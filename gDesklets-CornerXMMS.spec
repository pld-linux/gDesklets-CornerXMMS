
%define	pname	CornerXMMS

Summary:	A fancy desklet that allows you to control XMMS from the desktop
Summary(pl):	Ozdobny desklet pozwalaj±cy sterowaæ XMMS-em z pulpitu
Name:		gDesklets-%{pname}
Version:	0.0.5
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://gdesklets.gnomedesktop.org/files/%{pname}-%{version}.tar.bz2
# Source0-md5:	2714260a2a82005a814db703cf2ea854
URL:		http://gdesklets.gnomedesktop.org/categories.php?func=gd_show_app&gd_app_id=53
BuildRequires:	python >= 2.3
BuildRequires:	python-pygtk-gtk >= 1.99.14
Requires:	gDesklets
Requires:	python-xmms
Provides:	gDesklets-display
Provides:	gDesklets-sensor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_sensorsdir	%{_datadir}/gdesklets/Sensors
%define _displaysdir	%{_datadir}/gdesklets/Displays

%description
A fancy desklet that allows you to control XMMS from the desktop.

%description -l pl
Ozdobny desklet pozwalaj±cy sterowaæ XMMS-em z pulpitu.

%prep
%setup -q -n %{pname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sensorsdir},%{_displaysdir}/%{pname}}

./Install_%{pname}_Sensor.bin --nomsg \
	$RPM_BUILD_ROOT%{_sensorsdir}

cp -R gfx *.display $RPM_BUILD_ROOT%{_displaysdir}/%{pname}

rm -rf $RPM_BUILD_ROOT%{_sensorsdir}/%{pname}/{.*~,icons/.xvpics,po}
find $RPM_BUILD_ROOT%{_sensorsdir}/%{pname} -name "CVS" |xargs rm -rf

%py_comp $RPM_BUILD_ROOT%{_sensorsdir}
%py_ocomp $RPM_BUILD_ROOT%{_sensorsdir}

rm -f $RPM_BUILD_ROOT%{_sensorsdir}/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_sensorsdir}/%{pname}/*.py[co]
%{_displaysdir}/*
