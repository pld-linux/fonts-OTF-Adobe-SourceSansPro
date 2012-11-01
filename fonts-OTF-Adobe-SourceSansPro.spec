Summary:	Adobe Source Sans Pro - A set of OpenType fonts designed for user interfaces
Summary(pl.UTF-8):	Adobe Source Sans Pro - zbiór fontów OpenType zaprojektowanych do interfejsów użytkownika
Name:		fonts-OTF-Adobe-SourceSansPro
Version:	1.038
Release:	1
License:	OFL v1.1
Group:		Fonts
Source0:	http://downloads.sourceforge.net/sourcesans.adobe/SourceSansPro_FontsOnly-%{version}.zip
# Source0-md5:	9593b87c5fc8ec83118f87692b224fc2
Source1:	%{name}-fontconfig.conf
URL:		http://sourceforge.net/projects/sourcesans.adobe/
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         otffontsdir     %{_fontsdir}/OTF

%description
Source Sans is a set of OpenType fonts that have been designed to work
well in user interface (UI) environments, as well as in text setting
for screen and print.

%description -l pl.UTF-8
Source Sans to zbiór fontów OpenType, zaprojetowanych z myślą o
środowiskach interfejsów użytkownika (UI), a także składzie tekstu na
ekran i do druku.

%prep
%setup -q -n SourceSansPro_FontsOnly-%{version}

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
