%define module	Net-XMPP
%define name	perl-%{module}
%define version 1.02

Name:		%{name}
Version:	%{version}
Release:	%mkrel 1
Summary:	XMPP Perl Library
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}/
Source:         http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.bz2
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(XML::Stream)
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
Net::XMPP is a convenient tool to use for any perl script that would
like to utilize the XMPP Instant Messaging protocol.  While not a
client in and of itself, it provides all of the necessary back-end
functions to make a CGI client or command-line perl client feasible 
and easy to use.  Net::XMPP is a wrapper around the rest of the
official Net::XMPP::xxxxxx packages.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/Net
%{_mandir}/*/*
