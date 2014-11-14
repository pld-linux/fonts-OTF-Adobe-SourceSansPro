Summary:	Adobe Source Sans Pro - A set of OpenType fonts designed for user interfaces
Summary(pl.UTF-8):	Adobe Source Sans Pro - zbiór fontów OpenType zaprojektowanych do interfejsów użytkownika
Name:		fonts-OTF-Adobe-SourceSansPro
%define	ro_ver	2.010
%define	it_ver	1.065
Version:	%{ro_ver}_%{it_ver}
Release:	1
License:	OFL v1.1
Group:		Fonts
Source0:	https://github.com/adobe-fonts/source-sans-pro/archive/%{ro_ver}R-ro/%{it_ver}R-it/source-sans-pro-%{ro_ver}R-ro-%{it_ver}R-it.tar.gz
# Source0-md5:	5dfa6f327cdd4cb363f8887493696a4c
Source1:	%{name}-fontconfig.conf
URL:		http://adobe-fonts.github.io/source-sans-pro
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         otffontsdir     %{_fontsdir}/OTF

%description
Source Sans is a set of OpenType fonts that have been designed to work
well in user interface (UI) environments, as well as in text setting
for screen and print.

This package contains Roman fonts version %{ro_ver} and Italic fonts
version %{it_ver}.

%description -l pl.UTF-8
Source Sans to zbiór fontów OpenType, zaprojetowanych z myślą o
środowiskach interfejsów użytkownika (UI), a także składzie tekstu na
ekran i do druku.

Ten pakiet zawiera fonty podstawowe (Roman) w wersji %{ro_ver} oraz
fonty kursywy (Italic) w wersji %{it_ver}.

%prep
%setup -q -n source-sans-pro-%{ro_ver}R-ro-%{it_ver}R-it

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{otffontsdir},%{_datadir}/fontconfig/conf.avail,%{_sysconfdir}/fonts/conf.d}

install -p OTF/*.otf $RPM_BUILD_ROOT%{otffontsdir}
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/%{name}.conf
ln -s %{_datadir}/fontconfig/conf.avail/%{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d/

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%doc LICENSE.txt ReadMe.html SourceSansProReadMe.html
%{otffontsdir}/SourceSansPro-*.otf
%{_sysconfdir}/fonts/conf.d/%{name}.conf
%{_datadir}/fontconfig/conf.avail/%{name}.conf
