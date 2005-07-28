%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-dateutil
Version:        1.0
Release:        1%{?dist}
Summary:        Powerful extensions to the standard datetime module

Group:          Development/Languages
License:        Python Software Foundation License
URL:            https://moin.conectiva.com.br/DateUtil
#Source0:        https://moin.conectiva.com.br/DateUtil?action=AttachFile&do=get&target=python-dateutil-%{version}.tar.bz2
Source0:        python-dateutil-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python

%description
The dateutil module provides powerful extensions to the standard datetime
module available in Python 2.3+.

%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc example.py LICENSE NEWS README
%{python_sitelib}/dateutil/

%changelog
* Thu Jul 28 2005 Orion Poplawski <orion@cora.nwra.com> 1.0-1
- Update to 1.0

* Tue Jul 05 2005 Orion Poplawski <orion@cora.nwra.com> 0.9-1
- Initial Fedora Extras package
