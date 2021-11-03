from cx_Freeze import setup, Executable

executables = [Executable('main.py',targetName='windows_sys.exe',base='Win32GUI')]
options = {
    'build_exe': {
        'include_msvcr': True,
        'build_exe': 'build_windows',
    }
}
setup(name='hello_world',
      version='0.0.2',
      description='My Hello World App!',
      executables=executables,
      options=options)