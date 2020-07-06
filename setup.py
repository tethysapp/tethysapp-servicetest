from setuptools import setup, find_namespace_packages
import os


def find_resource_files(directory, relative_to=None):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            if relative_to is not None:
                paths.append(os.path.join(os.path.relpath(path, relative_to), filename))
            else:
                paths.append(os.path.join('..', path, filename))
    return paths


# -- Apps Definition -- #
app_package = 'servicetest'
release_package = 'tethysapp-' + app_package

# -- Python Dependencies -- #
dependencies = []

# -- Get Resource File -- #
resource_files = find_resource_files('tethysapp/' + app_package + '/templates', 'tethysapp/' + app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/public', 'tethysapp/' + app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/workspaces', 'tethysapp/' + app_package)


setup(
    name=release_package,
    version='0.0.4',
    description='This is a service Test Application',
    long_description='',
    keywords='Tethys,App,Services,Cool',
    author='Rohit Khattar',
    author_email='rohitkhattar@gmail.com',
    url='https://github.com/rfun/tethysapp-servicetest.git',
    license='BSD 3-Clause License',
    packages=find_namespace_packages(),
    package_data={'': resource_files},
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
)
