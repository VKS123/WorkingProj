# -*- mode: python -*-

block_cipher = None


a = Analysis(['main_runner.py'],
             pathex=['C:\\Users\\sbaid\\Documents\\SASA\\WorkingProj'],
             binaries=[],
             datas=[('img1.png','.'),('img2.png','.'),('img3.png','.'),('img4.png','.'),('rsakeygen.png','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main_runner',
          debug=False,
          strip=False,
          upx=True,
          console=True )

