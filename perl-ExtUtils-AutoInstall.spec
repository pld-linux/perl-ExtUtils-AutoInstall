#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	ExtUtils
%define		pnam	AutoInstall
Summary:	ExtUtils::AutoInstall - automatic install of dependencies via CPAN
Summary(pl.UTF-8):   ExtUtils::AutoInstall - automatyczna instalacja zależności z CPAN
Name:		perl-ExtUtils-AutoInstall
Version:	0.61
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	66f1696ee4dfb76cfe42a716da48e6f5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::AutoInstall Perl module lets module writers to specify a
more sophisticated form of dependency information than the PREREQ_PM
option offered by ExtUtils::MakeMaker.  Most notable features include:

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

%description -l pl.UTF-8
Moduł Perla ExtUtils::AutoInstall pozwala autorom modułów na
udostępnianie informacji o zależnościach w bardziej wyszukanej formie,
niż opcja PREREQ_PM obsługiwana przez ExtUtils::MakeMaker. Większość
godnych uwagi właściwości to:

- Umożliwienie użytkownikom na włączanie/wyłączanie zależności
  opcjonalnych.
- Wsparcie dla wartości domyślnych otrzymywanych poprzez sprawdzenie
  właściwości maszyny.
- Korzystanie z CPAN.pm do instalacji zależności w przypadku użycia
  spoza powłoki cpan.
- Automatyczne włączanie/wyłączanie stowarzyszonych testów.
- Podanie UNINST=1, gdy jest to bezpieczne i prawdopodobnie potrzebne.
- Sprawdzenie MANIFEST, aby uniknąć niepotrzebnego przeszukiwania
  EXE_FILES.
- Wykorzystanie CPANPLUS i/lub Sort::Versions, gdy jest to możliwe.
- Udostępnienie celów Makefile.PL check-only i skip-all.
- Udostępnienie celów Makefile check-only i install-only.
- Wykorzystanie polecenia 'sudo', gdy jest ono dostępne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"ExtUtils::AutoInstall")' \
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
%doc AUTHORS Changes README TODO
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
