#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	AutoInstall
Summary:	ExtUtils::AutoInstall - automatic install of dependencies via CPAN
Summary(pl):	ExtUtils::AutoInstall - automatyczna instalacja zale¿no¶ci z CPAN
Name:		perl-ExtUtils-AutoInstall
Version:	0.57
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5f63a9baae27f8020822913e4f01c882
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Modu³ Perla ExtUtils::AutoInstall pozwala autorom modu³ów na
udostêpnianie informacji o zale¿no¶ciach w bardziej wyszukanej formie,
ni¿ opcja PREREQ_PM obs³ugiwana przez ExtUtils::MakeMaker. Wiêkszo¶æ
godnych uwagi w³a¶ciwo¶ci to:

- Umo¿liwienie u¿ytkownikom na w³±czanie/wy³±czanie zale¿no¶ci
  opcjonalnych.
- Wsparcie dla warto¶ci domy¶lnych otrzymywanych poprzez sprawdzenie
  w³a¶ciwo¶ci maszyny.
- Korzystanie z CPAN.pm do instalacji zale¿no¶ci w przypadku u¿ycia
  spoza pow³oki cpan.
- Automatyczne w³±czanie/wy³±czanie stowarzyszonych testów.
- Podanie UNINST=1, gdy jest to bezpieczne i przwdopodobnie potrzebne.
- Sprawdzenie MANIFEST, aby unikn±æ niepotrzebnego przeszukiwania
  EXE_FILES.
- Wykorzystanie CPANPLUS i/lub Sort::Versions, gdy jest to mo¿liwe.
- Udostêpnienie celów Makefile.PL check-only i skip-all.
- Udostêpnienie celów Makefile check-only i install-only.
- Wykorzystanie polecenia 'sudo', gdy jest ono dostêpne.

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
