Name:		openconnect
Version:	0.99
Release:	2%{?dist}
Summary:	Open client for Cisco AnyConnect VPN

Group:		Applications/Internet
License:	LGPLv2+
URL:		http://git.infradead.org/users/dwmw2/openconnect.git
Source0:	ftp://ftp.infradead.org/pub/openconnect/openconnect-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	openssl-devel libxml2-devel gtk2-devel GConf2-devel dbus-devel
Requires:	vpnc

%description
This package provides a client for Cisco's "AnyConnect" VPN, which uses
HTTPS and DTLS protocols.

%prep
%setup -q

%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8
install -m0644 openconnect.8 $RPM_BUILD_ROOT/%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/openconnect
%{_libexecdir}/nm-openconnect-auth-dialog
%{_mandir}/man8/*
%doc TODO COPYING.LGPL



%changelog
* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 0.99-2
- rebuild with new openssl

* Tue Dec 16 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.99-1
- Update to 0.99.
- Fix BuildRequires

* Mon Nov 24 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.98-1
- Update to 0.98.

* Thu Nov 13 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.97-1
- Update to 0.97. Add man page, validate server certs.

* Tue Oct 28 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.96-1
- Update to 0.96. Handle split-includes, MacOS port, more capable SecurID.

* Thu Oct 09 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.95-1
- Update to 0.95. A few bug fixes.

* Thu Oct 09 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.94-3
- Include COPYING.LGPL file

* Mon Oct 07 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.94-2
- Fix auth-dialog crash

* Mon Oct 06 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.94-1
- Take cookie on stdin so it's not visible in ps.
- Support running 'script' and passing traffic to it via a socket
- Fix abort when fetching XML config fails

* Sun Oct 05 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.93-1
- Work around unexpected disconnection (probably OpenSSL bug)
- Handle host list and report errors in NM auth dialog

* Sun Oct 05 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.92-1
- Rename to 'openconnect'
- Include NetworkManager auth helper

* Thu Oct 02 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.91-1
- Update to 0.91

* Thu Oct 02 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.90-1
- First package
