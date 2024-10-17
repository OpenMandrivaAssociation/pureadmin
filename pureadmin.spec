%define Werror_cflags %nil

%define	name	pureadmin
%define	version	0.4
%define release	6

Name:		%name
Version:	%version
Release:	%release
Summary:	PureFTPd graphical manager
License:	GPL
Group:		Networking/File transfer
Source0:	http://dl.sourceforge.net/purify/%{name}-%{version}.tar.bz2
URL:		https://purify.sourceforge.net/
BuildRequires:	fam-devel pkgconfig intltool autoconf2.5
BuildRequires:	pkgconfig(libglade-2.0)
Requires:	pure-ftpd

%description
PureAdmin is a graphical tool used to make the management of PureFTPd
a little easier. It uses the GTK+2.x widgets for its GUI and thus are
not dependent on a specific desktop environment such as GNOME or KDE.
It is, however, designed with the GNOME Human Interface Guidelines in
mind so it should integrate nicely with at least GNOME.

%prep
%setup -q

%build
%configure2_5x
%make LIBS="-lX11 -lpthread -lfam -ldl -lcrypt -lm"

%install
%makeinstall_std
%find_lang %{name}

%post
gtk-update-icon-cache --force --quiet %{_datadir}/icons/hicolor

%postun
if [ "$1" = "0" ]; then
  gtk-update-icon-cache --force --quiet %{_datadir}/icons/hicolor
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/*/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/pureadmin.desktop
