Name:		python-xxhash
Version:	3.4.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/x/xxhash/xxhash-%{version}.tar.gz
Summary:	Python binding for xxHash
URL:		https://pypi.org/project/xxhash/
License:	BSD
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	pkgconfig(libxxhash)
BuildRequires:	pkgconfig(python3)

%description
Python binding for xxHash

%prep
%autosetup -p1 -n xxhash-%{version}

%build
%py_build

%install
%py_install

%files
%{py_platsitedir}/xxhash
%{py_platsitedir}/xxhash-*.*-info
