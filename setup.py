from setuptools import setup

setup(
    name="steemconnect_auth",
    version='0.0.3',
    description='A django application to login with steemconnect.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='hakancelik96',
    author_email='hakancelik96@outlook.com',
    packages=["steemconnect_auth"],
    include_package_data=True,
    install_requires=["steem-connect"],
    url="https://github.com/coogger/django_steemconnect",
    license='MIT',
    zip_safe=False,
    keywords="steemconnect,django steemconnect,steem,django steem,login steemconnect",
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
