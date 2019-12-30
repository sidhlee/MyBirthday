# -*- mode: python -*-

block_cipher = None


a = Analysis(['MyBirthday.py'],
             pathex=['/Users/hayounlee/PycharmProjects/MyBirthday'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MyBirthday',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='MyBirthday.icns')
app = BUNDLE(exe,
             name='MyBirthday.app',
             icon='MyBirthday.icns',
             bundle_identifier=None,
             info_plist={
        'NSHighResolutionCapable': 'True'
        },)
