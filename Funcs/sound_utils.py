import asyncio

import comtypes
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume


class SoundUtils:

    @staticmethod
    async def get_audio_sessions():
        """
        Получает список всех приложений, которые сейчас используют звук.
        """
        def _get_sessions_sync():
            # Инициализируем COM для этого потока
            comtypes.CoInitialize()
            try:
                sessions_list = []
                sessions = AudioUtilities.GetAllSessions()
                for session in sessions:
                    volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                    if session.Process:
                        name = session.Process.name()
                        current_vol = volume.GetMasterVolume()
                        is_muted = volume.GetMute()

                        sessions_list.append({
                            "name": name,
                            "volume": round(current_vol * 100),
                            "is_muted": is_muted
                        })
                return sessions_list
            finally:
                # Освобождаем ресурсы COM
                comtypes.CoUninitialize()

        return await asyncio.to_thread(_get_sessions_sync)

    @staticmethod
    async def set_app_volume(app_name: str, change: int):
        """
        Изменяет громкость приложения.
        """
        def _set_vol_sync():
            # Инициализация COM
            comtypes.CoInitialize()
            try:
                sessions = AudioUtilities.GetAllSessions()
                for session in sessions:
                    if session.Process and session.Process.name() == app_name:
                        volume = session._ctl.QueryInterface(
                            ISimpleAudioVolume)

                        current = volume.GetMasterVolume()
                        new_vol = min(1.0, max(0.0, current + (change / 100)))

                        volume.SetMasterVolume(new_vol, None)
                        return True
                return False
            finally:
                # Очистка COM
                comtypes.CoUninitialize()

        return await asyncio.to_thread(_set_vol_sync)

    @staticmethod
    async def toggle_mute(app_name: str):
        """Включает/выключает звук у приложения"""
        def _mute_sync():
            # Инициализация COM
            comtypes.CoInitialize()
            try:
                sessions = AudioUtilities.GetAllSessions()
                for session in sessions:
                    if session.Process and session.Process.name() == app_name:
                        volume = session._ctl.QueryInterface(
                            ISimpleAudioVolume)
                        current_mute = volume.GetMute()
                        volume.SetMute(not current_mute, None)
                        return True
                return False
            finally:
                # Очистка COM
                comtypes.CoUninitialize()

        return await asyncio.to_thread(_mute_sync)
