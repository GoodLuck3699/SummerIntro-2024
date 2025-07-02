# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['AppleClicker.py'],
    pathex=[],
    binaries=[],
    datas=[('Achievement1.png', '.'), ('Achievement2.png', '.'), ('Achievement3.png', '.'), ('Achievement4.png', '.'), ('achievement5.png', '.'), ('AchievementSound.wav', '.'), ('BackfroundMusicImage.png', '.'), ('preAchievement1.png', '.'), ('preAchievement2.png', '.'), ('preAchievement3.png', '.'), ('preAchievement4.png', '.'), ('preAchievement5.png', '.'), ('Credits.png', '.'), ('Demon.png', '.'), ('FactoryWorker.png', '.'), ('Farmer1.png', '.'), ('FreeApple2.png', '.'), ('golden apple.png', '.'), ('NoMusicImage.png', '.'), ('NoSoundImage.png', '.'), ('Question.png', '.'), ('settingsButton.png', '.'), ('SoundImage.png', '.'), ('Sunset.png', '.'), ('Tycoon.png', '.'), ('UpperClass.png', '.'), ('Goldberg Variations, BWV 988 - 22 - Variatio 21 Canone alla Settima.wav', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='AppleClicker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
