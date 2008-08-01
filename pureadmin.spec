%define	name	pureadmin
%define	version	0.4
%define	release	%mkrel 4

Name:		%name
Version:	%version
Release:	%release
Summary:	PureFTPd graphical manager
License:	GPL
Group:		Networking/File transfer
Source0:	http://dl.sourceforge.net/purify/%{name}-%{version}.tar.bz2
URL:		http://purify.sourceforge.net/
BuildRequires:	fam-devel pkgconfig intltool autoconf2.5 libglade2.0-devel
Requires:	pure-ftpd
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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
%make

%install
rm -rf %buildroot
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %buildroot

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
