#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	AutoInstall
Summary:	ExtUtils::AutoInstall - Automatic install of dependencies via CPAN
#Summary(pl):	
Name:		perl-ExtUtils-AutoInstall
Version:	0.52
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	14517486c3ac86683bf9401bdfd8f3ce
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::AutoInstall lets module writers to specify a more sophisticated
form of dependency information than the PREREQ_PM option offered by
ExtUtils::MakeMaker.  Most notable features include:

- Letting the user enable/disable optional dependencies.
- Support sane defaults by probing for the machine's capability.
- If not inside a cpan shell, use CPAN.pm to install dependencies.
- Enable/disable the associated tests automatically.
- Supply UNINST=1 when it is safe and possibly needed.
- Checks MANIFEST to avoid unnecessary grepping of EXE_FILES.
- Utilizes CPANPLUS and/or Sort::Versions where feasible.
- Offers check-only and skip-all Makefile.PL targets.
- Offers check-only and install-only Makefile targets.
- Take advantage of the 'sudo' command where available.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"ExtUtils::AutoInstall")' \
	INSTALLDIRS=vendor
%{__make}

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changes README TODO
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
