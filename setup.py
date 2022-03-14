from setuptools import setup
from midas2 import version


setup(name='midas2',
      version=version,
      description='https://github.com/czbiohub/MIDAS2.0/wiki/MIDAS-2.0',
      url='https://github.com/czbiohub/MIDAS2.0',
      author='Chunyu Zhao, Boris Dimitrov',
      author_email='chunyu.zhao@czbiohub.org',
      license='MIT',
      packages=['midas2', 'midas2/subcommands', 'midas2/common', 'midas2/params', 'midas2/models'],
      install_requires=[],
      dependency_links=[],
      entry_points={
        'console_scripts': [
          'midas2 = midas2.__main__:main'
        ]
      },
      zip_safe=False
)
