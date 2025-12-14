%define module xxhash

Name:		python-xxhash
Version:	3.6.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/x/%{module}/%{module}-%{version}.tar.gz
Summary:	Python binding for xxHash
URL:		https://pypi.org/project/xxhash/
License:	BSD
Group:		Development/Python
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(libxxhash)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

%description
Python binding for xxHash

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py_build

%install
%py_install

%files
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
