Name:		influxdb-python
Version:	0.1.12
Release:	3kaji0.2
Summary:	Python client for InfluxDB

Group:		Network
License:	AGPLv3+
URL:		https://github.com/kaji-project/influxb-python
Source0:	%{name}_%{version}.orig.tar.gz

BuildArch:  noarch

BuildRequires: python-setuptools
Requires: python-requests

# use to remove the dependency added by rpmbuild on python(abi)
AutoReqProv: no

%description
Python client for InfluxDB
 .
 This is the Python 2 compatible package.

%prep
%setup -q

%build


%install
rm -rf %{buildroot}/*
%{__python} setup.py install -O1 --root=%{buildroot}
rm -rf  %{buildroot}/%{python_sitelib}/tests


%files
%{python_sitelib}/influxdb*

%changelog
* Wed Apr 29 2015 Sébastien Coavoux <sebastien.coavoux@savoirfairelinux.com> 0.1.12-3kaji0.2
- Fix Packaging

* Wed Apr 29 2015 Sébastien Coavoux <sebastien.coavoux@savoirfairelinux.com> 0.1.12-2kaji0.2
- New Release

* Wed Jan 28 2015 Sébastien Coavoux <sebastien.coavoux@savoirfairelinux.com> 0.1.12-1kaji0.2
- Initial Package
