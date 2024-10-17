Summary:	Web site feedback mod_spin application
Name:		spin_feedback
Version:	1.2.0
Release:	%mkrel 3
Group:		System/Servers
License:	LGPLv2+
URL:		https://www.rexursive.com/software/modspin/applications.html
Source0:	ftp://ftp.rexursive.com/pub/spinapps/feedback/%{name}-%{version}.tar.bz2
Requires:	apache-mod_spin >= 1.1.8
BuildRequires:	apache-devel
BuildRequires:	apache-mod_spin-devel >= 1.1.8
BuildRequires:	autoconf2.5
BuildRequires:	bison
BuildRequires:	doxygen
BuildRequires:	file
BuildRequires:	file-devel
BuildRequires:	flex >= 2.5.33
BuildRequires:	libapreq-devel >= 2.07
BuildRequires:	libesmtp-devel >= 1.0.3r1
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The application collects parameters of an (X)HTML form, as either
multipart/form-data or application/x-www-form-urlencoded, validates them,
stores them into an SQL database and e-mails to a designated e-mail address.
E-mailing of attachments is supported, but only the name of the uploaded file
is stored into the database.

%prep

%setup -q -n %{name}-%{version}

%build
%serverbuild
libtoolize --copy --force --automake; aclocal -I m4; autoheader; autoconf; automake --add-missing --copy

%configure2_5x \
    --disable-static \
    --enable-packager \
    --libdir=%{_libdir}/spinapps

%make

%install
rm -rf %{buildroot}

%makeinstall_std

install -d %{buildroot}%{_sysconfdir}/httpd/modules.d
install -m0644 spin_feedback.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/A66_spin_feedback.conf

# cleanup
rm -f %{buildroot}%{_libdir}/spinapps/spin_feedback.*a
rm -rf %{buildroot}%{_docdir}/%{name}-%{version}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING ChangeLog NEWS README create-feedback*.sql
%config(noreplace) %{_sysconfdir}/httpd/modules.d/A66_spin_feedback.conf
%config(noreplace) %{_sysconfdir}/spinapps/spin_feedback.xml
%{_libdir}/spinapps/spin_feedback.so
%{_datadir}/%{name}

