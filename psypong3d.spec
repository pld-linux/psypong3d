Summary:	3d pong clone game
Summary(pl.UTF-8):	trójwymiarowa wersja gry pong
Name:		psypong3d
Version:	0.9
Release:	1
License:	GPL v3
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/psypong3d/%{name}-%{version}.tar.bz2
# Source0-md5:	c0f5891a306dbcfed07e2e513a854362
Source1:	%{name}.desktop
Patch0:		%{name}-paths.patch
URL:		http://psypong3d.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PSY PONG 3D, is a three dimensional Pong clone made in C, using
OpenGL/GLUT.

%description -l pl.UTF-8
PSY PONG 3D to trójwymiarowy klon gry Pong napisany w C z
wykorzystaniem OpenGL/GLUT.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C src \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_datadir}/games/%{name}/textures}

install src/pp3d $RPM_BUILD_ROOT%{_bindir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install src/textures/* $RPM_BUILD_ROOT%{_datadir}/games/%{name}/textures

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_datadir}/games/%{name}
