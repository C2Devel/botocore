%global pkgname botocore
%define buildid @BUILDID@

Name:           python-%{pkgname}
# NOTICE - Updating this package requires updating python-boto3
Version:        1.20.14
Release:        CROC2%{?buildid}%{?dist}
Summary:        Low-level, data-driven core of boto 3

License:        ASL 2.0
URL:            https://github.com/C2Devel/botocore.git
Source0:        https://pypi.io/packages/source/b/botocore/botocore-%{version}.tar.gz
BuildArch:      noarch

%description
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.

%package -n     python2-%{pkgname}
Summary:        Low-level, data-driven core of boto 3
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Provides:       python2-%{pkgname}
Requires:       python2-jmespath >= 0.7.1
Requires:       python2-dateutil >= 2.1

%description -n python2-%{pkgname}
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.

%package -n     python%{python3_pkgversion}-%{pkgname}
Summary:        Low-level, data-driven core of boto 3
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Provides:       python%{python3_pkgversion}-%{pkgname}
Requires:       python%{python3_pkgversion}-jmespath >= 0.7.1
Requires:       python%{python3_pkgversion}-dateutil >= 2.1

%description -n python%{python3_pkgversion}-%{pkgname}
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.

%prep
%setup -q -n %{pkgname}-%{version}
rm -rf %{pkgname}.egg-info
# Remove online tests
rm -rf tests/integration

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-%{pkgname}
%doc README.rst
%license LICENSE.txt
%{python2_sitelib}/%{pkgname}/
%{python2_sitelib}/%{pkgname}-*.egg-info/

%files -n python%{python3_pkgversion}-%{pkgname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{pkgname}/
%{python3_sitelib}/%{pkgname}-*.egg-info/

%changelog
* Mon Jun 28 2021 Max Kotov <makotov@croc.ru> - 1.20.14-CROC2
- Introduce KS Public API
* Wed Feb 24 2021 Alexander Chernev <achernev@croc.ru> - 1.20.14-CROC1
- Update to latest botocore - 1.20.14
