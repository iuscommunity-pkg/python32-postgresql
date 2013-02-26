%global __python32 /usr/bin/python3.2
%{!?python32_sitearch: %global python32_sitearch %(%{__python32} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           python32-postgresql
Version:        1.1.0
Release:        2.ius%{?dist}
Summary:        Connect to PostgreSQL with Python 3

Group:          Applications/Databases
License:        BSD
URL:            http://python.projects.postgresql.org/
Source0:        http://pypi.python.org/packages/source/p/py-postgresql/py-postgresql-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python32-devel

%description
py-postgresql is a Python 3 package providing modules to work with PostgreSQL.
This includes a high-level driver, and many other tools that support a
developer working with PostgreSQL databases.

%prep
%setup -q -n py-postgresql-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python32} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python32} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE README
%{python32_sitearch}/*


%changelog
* Fri Oct 26 2012 Ben Harper <ben.harper@rackspace.com> 1.1.0-2.ius
- increase release to correct bad push to testing repo only

* Thu Oct 25 2012 Ben Harper <ben.harper@rackspace.com> 1.1.0-1.ius
- Latest Sources from Upstream
- Changed source to pypi per http://pgfoundry.org/pipermail/python-general/2012-October/001002.html\

* Tue Jul 31 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0.4-1.ius
- New package for python32
