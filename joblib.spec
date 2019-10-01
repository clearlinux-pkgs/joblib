#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : joblib
Version  : 0.14.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/0a/ae/89d32b92903241468d9e993d05c49e8e7d58bdc3db51ed276b01786760ac/joblib-0.14.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/0a/ae/89d32b92903241468d9e993d05c49e8e7d58bdc3db51ed276b01786760ac/joblib-0.14.0.tar.gz
Summary  : Lightweight pipelining: using Python functions as pipeline jobs.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: joblib-license = %{version}-%{release}
Requires: joblib-python = %{version}-%{release}
Requires: joblib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
|PyPi| |Travis| |AppVeyor| |Codecov|
.. |Travis| image:: https://travis-ci.org/joblib/joblib.svg?branch=master
:target: https://travis-ci.org/joblib/joblib
:alt: Travis build status

%package license
Summary: license components for the joblib package.
Group: Default

%description license
license components for the joblib package.


%package python
Summary: python components for the joblib package.
Group: Default
Requires: joblib-python3 = %{version}-%{release}

%description python
python components for the joblib package.


%package python3
Summary: python3 components for the joblib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the joblib package.


%prep
%setup -q -n joblib-0.14.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569947021
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/joblib
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/joblib/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/joblib/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
