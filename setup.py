from setuptools import setup

with open("README.rst", "r") as f:
    long_description = f.read()

setup(
    name='trackfilter',
    version='1.2.0',
    description='Remove YouTube-related garbage from song titles.',
    long_description=long_description,
    url='https://github.com/mirrorfm/trackfilter',
    author='Stephane Bruckert',
    author_email='stephane.bruckert@gmail.com',
    license='MIT',
    packages=['trackfilter'],
    install_requires=[],
    project_urls={
        'Documentation': 'https://trackfilter.readthedocs.io/',
        'Changelog': 'https://trackfilter.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://github.com/mirrorfm/trackfilter/issues',
    },
    zip_safe=False,
    python_requires='~=3.8',
    test_suite='nose.collector',
    tests_require=['nose2'],
    entry_points={
        'console_scripts': [
            'trackfilter = trackfilter.cli:split_artist_and_track_name',
        ]
    }
)
