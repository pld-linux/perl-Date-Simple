#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Date
%define		pnam	Simple
Summary:	Date::Simple - a simple date object
Summary(pl.UTF-8):	Date::Simple - prosty obiekt daty
Name:		perl-Date-Simple
Version:	3.03
Release:	1
License:	GPL v2+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	436049dc2c7dfd8423d8bcc807248b31
URL:		http://search.cpan.org/dist/Date-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module may be used to create simple date objects. It only handles
dates within the range of Unix time. It will only allow the creation
of objects for valid dates. Attempting to create an invalid date will
return undef.

%description -l pl.UTF-8
Ten moduł może być używany do tworzenia prostych obiektów daty.
Obsługuje tylko daty z uniksowego przedziału czasu. Pozwala stworzyć
obiekty tylko dla poprawnych dat - przy próbie stworzenia błędnej daty
zwróci undef.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL noxs \
	INSTALLDIRS=vendor

%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Date/Simple.pm
%{perl_vendorlib}/Date/Simple
%{_mandir}/man3/*
