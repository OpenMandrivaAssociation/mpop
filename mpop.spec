Summary:	A POP3 client that retrieves mail from POP3 mailboxes
Name:		mpop
Version:	1.0.20
Release:	%mkrel 1
License:	GPLv2+
Group:		Networking/Mail
URL:		http://mpop.sourceforge.net/
Source0:	http://heanet.dl.sourceforge.net/sourceforge/mpop/%{name}-%{version}.tar.bz2
BuildRequires:	libgcrypt-devel
BuildRequires:	libgnutls-devel
BuildRequires:	libgpg-error-devel
#BuildRequires:	libgsasl-devel <- not packaged yet, why?
BuildRequires:	libidn-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
rm -rf %{buildroot}
%makeinstall
%find_lang %{name}

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS NOTES README THANKS
%{_bindir}/%{name}
%{_infodir}/*
%{_mandir}/man1/*
