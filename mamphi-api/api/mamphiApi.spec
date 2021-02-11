# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['mamphiApi.py'],
             pathex=['C:\\Users\\biocl\\Desktop\\Beauclair\\USB DISK\\Master\\FH_DO\\PyDev\\sms-sose-2019-mamphi-administration\\mamphi-api\\api'],
             binaries=[],
             datas=[('./data/mamphi.db', 'data')],
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
          [],
          exclude_binaries=True,
          name='mamphiApi',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          icon='./favicon.ico',
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='mamphiApi')
