from setuptools import setup

setup(
    name='django_langlink',
    version='0.1.a1',
    description='Abstract language model and management command to populate language model',
    url='https://github.com/payamnj/django-langlink',
    author='Payam Najafizadeh',
    author_email='payam.nj@gmail.com',
    license='New BSD',
    packages=['langlink', 'langlink.management',
        'langlink.management.commands'],
    requires=['django(>=1.8)'],)
