%define module xxhash

Name:		python-xxhash
Version:	3.8.1
Release:	2
Summary:	Python binding for xxHash
License:	BSD
Group:		Development/Python
URL:		https://pypi.org/project/xxhash
Source0:	https://files.pythonhosted.org/packages/source/x/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(libxxhash)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

%description
Python binding for xxHash

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
