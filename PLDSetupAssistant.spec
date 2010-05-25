#
%define		kdever		4.4.3

Summary:	PLD Setup Assistant
Summary(pl.UTF-8):	Asystent konfiguracji PLD
Name:		PLDSetupAssistant
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	eda58a079150838a503c232e06a0aa8c
#URL:		http://
# leave only required ones
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	rpmbuild(macros) >= 1.293
Requires:	kde4-knetworkmanager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD Setup Assistant.

%description -l pl.UTF-8
Asystent konfiguracji PLD.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pldsetupassistant
%{_datadir}/apps/pldsetupassistant
