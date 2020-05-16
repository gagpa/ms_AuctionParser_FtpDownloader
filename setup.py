from setuptools import setup, find_packages

requirements = [line.strip() for line in open('requirements.txt').readlines()]
packages = find_packages('packages') + find_packages(include=['ms_app']) + \
           ['ms_app/' + dir_pack for dir_pack in find_packages('ms_app')]

setup(name='FtpDownloader_packages',
      version='1.0.3',
      author='oFry',
      entry_points={'console_scripts': ['ms_downloader = activate:main']},
      packages=packages,
      package_dir={'ftp_downloader': 'packages/ftp_downloader'},
      data_files=['activate.py'],
      install_requires=requirements,
      )
