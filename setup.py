from setuptools import setup

setup(
    name='storage_timeline_hurst_indicator',
    version='1.3',
    author='Illiatea',
    author_email='illiatea2@gmail.com',
    install_requires=['numpy'],
    py_modules=['storage_timeline_hurst_indicator.indicators', 'storage_timeline_hurst_indicator.processor']
)
