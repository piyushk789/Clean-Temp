from setuptools import setup, find_packages

setup(
    name='TempCleaner',
    version='0.1.5',
    author='Kartikey Baghel',
    author_email='kartikeybaghel@hotmail.com',
    description="""The "TempCleaner" application provides a simple and user-friendly interface that allows users to quickly scan their computer for temporary files and folders.""",
    long_description=""""TempCleaner" is an application designed to help users efficiently clean up temporary files and folders from their computer. Temporary files are created by various applications and processes on a computer and are intended to be used for a short period of time. However, these files can accumulate over time, taking up valuable disk space and slowing down the computer's performance.""",
    packages=find_packages(),
    keywords=['clean temp', 'TempCleaner', 'Temp Clean', 'Temp Cleaner', 'temp', 'clean', 'temporary', 'temporary files clean', 'windows', 'window', 'clean temporary file', 'clean temporary file for windows'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows"
    ]
)