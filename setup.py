import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='exchanges_rates_async',
    version='0.1',
    author='v1ack',
    author_email='kirilkin12@gmail.com',
    description='Provides async http server with auto update',
    long_description=long_description,
    install_requires=['aiomisc', 'aiohttp'],

    packages=setuptools.find_packages(),
    python_requires='>=3.6'
)
