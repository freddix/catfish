Summary:	Versatile file searching tool
Name:		catfish
Version:	0.4.0.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://launchpad.net/catfish-search/0.4/0.4.0.2/+download/%{name}-%{version}.tar.bz2
# Source0-md5:	d80eb544a12dbee2b2c84b63c4903eea
Patch0:		%{name}-build.patch
Patch1:		%{name}-env.patch
URL:		http://twotoasts.de/index.php/catfish/
BuildRequires:	desktop-file-utils
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	gtk+3
Requires:	python-pygobject
Requires:	python-pyxdg
Suggests:	mlocate
Suggests:	tracker
Suggests:	zeitgeist
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Catfish is a GTK+ search utility written in python. It's search
is powered by find and locate, with search suggestions provided
by zeitgeist.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./configure \
	--prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/catfish
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/catfish
%{__rm} $RPM_BUILD_ROOT%{_datadir}/catfish/catfish.py

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc/catfish

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/catfish.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/catfish
%dir %{_datadir}/catfish
%{_datadir}/catfish/*.glade
%{_datadir}/catfish/*.py[co]
%{_datadir}/catfish/*.svg
%{_datadir}/catfish/locale

%{_desktopdir}/catfish.desktop
%{_iconsdir}/hicolor/*/apps/catfish.svg

