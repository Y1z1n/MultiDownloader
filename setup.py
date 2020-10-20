from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='MultiDownload',
  version='0.2.3',
  description='A libary to download media from social media like twitter.com, instagram.com, snapchat.com and more will be added with the next updates',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Yazan Talib',
  author_email='y1z1n.xx@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Downloader, Multi downloader, Social media downloader', 
  packages=find_packages(),
  install_requires=['requests'] 
)
