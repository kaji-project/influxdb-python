Name:		influxdb-python
Version:	0.1.12
Release:	1kaji0.2
Summary:	Python client for InfluxDB

Group:		Network
License:	AGPLv3+
URL:		https://github.com/kaji-project/influxb-python
Source0:	%{name}_%{version}.orig.tar.gz

BuildArch:  noarch

BuildRequires: python-setuptools
Requires: python

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
%{python_sitelib}/influxdb
%{python_sitelib}/influxdb-%{version}-*.egg-info

%changelog
* Wed Jan 28 2015 Sébastien Coavoux <sebastien.coavoux@savoirfairelinux.com> 0.1.12-1kaji0.2
- Initial Package
