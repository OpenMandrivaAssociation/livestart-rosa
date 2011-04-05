Summary:	Livestart rosa script
Name:		livestart-rosa
Version:	1.0.0
Release:	1
BuildArch:	noarch
License:	GPL
Group:		System/Configuration/Other
Source10:	checkflashboot
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Small script checking if system was started from a
flash drive and creating a config for draklive-install.

%post
%_add_service_helper checkflashboot

%files
%defattr(-,root,root)
%attr(755,root,root) %_sysconfdir/init.d/checkflashboot

#--------------------------------------------------------------------

%install
rm -rf %buildroot 

mkdir -p %buildroot%_sysconfdir/init.d/
cp %SOURCE10 %buildroot%_sysconfdir/init.d/

