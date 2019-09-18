Summary:	Complex error function library
Summary(pl.UTF-8):	Biblioteka zespolonej funkcji błędu
Name:		libcerf
Version:	1.13
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://jugit.fz-juelich.de/mlz/libcerf/-/tags
Source0:	https://jugit.fz-juelich.de/mlz/libcerf/uploads/924b8d245ad3461107ec630734dfc781/%{name}-%{version}.tgz
# Source0-md5:	2c8466e79ca9a50f98d3dee1f81aa6dd
Patch0:		%{name}-libdir.patch
URL:		https://jugit.fz-juelich.de/mlz/libcerf
BuildRequires:	cmake >= 3.6
BuildRequires:	gcc >= 1:3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Complex error function library.

%description -l pl.UTF-8
Biblioteka zespolonej funkcji błędu.

%package devel
Summary:	Header files for libcerf library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcerf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcerf library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcerf.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged in man format
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libcerf

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG COPYING README
%attr(755,root,root) %{_libdir}/libcerf.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libcerf.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcerf.so
%{_includedir}/cerf.h
%{_pkgconfigdir}/libcerf.pc
%{_mandir}/man3/cdawson.3*
%{_mandir}/man3/cerf.3*
%{_mandir}/man3/cerfc.3*
%{_mandir}/man3/cerfcx.3*
%{_mandir}/man3/cerfi.3*
%{_mandir}/man3/dawson.3*
%{_mandir}/man3/erfcx.3*
%{_mandir}/man3/erfi.3*
%{_mandir}/man3/im_w_of_z.3*
%{_mandir}/man3/voigt.3*
%{_mandir}/man3/voigt_hwhm.3*
%{_mandir}/man3/w_of_z.3*
