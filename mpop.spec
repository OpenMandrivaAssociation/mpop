Summary:	A POP3 client that retrieves mail from POP3 mailboxes
Name:		mpop
Version:	1.0.27
Release:	3
License:	GPLv2+
Group:		Networking/Mail
URL:		http://mpop.sourceforge.net/
Source0:	http://heanet.dl.sourceforge.net/sourceforge/mpop/%{name}-%{version}.tar.bz2
BuildRequires:	libgcrypt-devel
BuildRequires:	gnutls-devel
BuildRequires:	libgpg-error-devel
BuildRequires:	libgsasl-devel 
#<- not packaged yet, why?
BuildRequires:	libidn-devel
BuildRequires:	zlib-devel

%description
mpop is a small, fast, and portable POP3 client. Its features include
header-based email filtering (filter junk mail before downloading it), delivery
to mbox files, maildir folders, or a mail delivery agent, a very fast POP3
implementation, many authentication methods, and good support for TLS/SSL.

%prep
%setup -q

%build
%configure2_5x \
    --enable-threads=pth \
    --disable-rpath \
    --with-ssl=gnutls \
    --with-libgnutls-prefix=%{_prefix} \
    --with-libidn \
    --with-libidn-prefix=%{_prefix}

#    --with-libgsasl \
#    --with-libgsasl-prefix=%{_prefix} \

%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS NOTES README THANKS
%{_bindir}/%{name}
%{_infodir}/*
%{_mandir}/man1/*


%changelog
* Thu May 03 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.27-1
+ Revision: 795257
- version update 1.0.27

* Wed May 11 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.0.24-1
+ Revision: 673658
- new version 1.0.24

* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 1.0.23-1
+ Revision: 645307
- update to new version 1.0.23

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.20-2mdv2011.0
+ Revision: 612945
- the mass rebuild of 2010.1 packages

* Tue Mar 30 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.0.20-1mdv2010.1
+ Revision: 529918
- Update to 1.0.20

* Tue Nov 17 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.19-1mdv2010.1
+ Revision: 466864
- 1.0.19 (fixes CVE-2009-3941)

* Wed Jun 17 2009 Jérôme Brenier <incubusss@mandriva.org> 1.0.17-1mdv2010.0
+ Revision: 386784
- update to new version 1.0.17

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.0.7-4mdv2009.0
+ Revision: 252964
- rebuild

* Wed Jan 23 2008 Funda Wang <fwang@mandriva.org> 1.0.7-2mdv2008.1
+ Revision: 156971
- rebuild

* Thu Jan 03 2008 Olivier Blin <blino@mandriva.org> 1.0.7-1mdv2008.1
+ Revision: 140963
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

