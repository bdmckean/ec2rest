from distutils.core import setup

setup(
	name='ec2rest',
      	version='0.1',
      	description='submits a command to ec2 rest IF and adds all the security info',
      	url='http://github.com/co-bri/ec2rest',
      	author='Brian McKean',
      	author_email='brian@rethlasoft.com',
      	license='MIT',
      	packages=['ec2rest'],
      	zip_safe=False)
	keywords = ["AWS", "REST"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
	"Development Status :: 2 - Pre-Alpha ",	
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description = """\
Packages AWS EC2 REST commands with secrity wrapper
	REST commands supported: 
		DescribeInstances
-------------------------------------
his version requires Python 3 or later; a Python 2 version is not yet available.
"""
)
