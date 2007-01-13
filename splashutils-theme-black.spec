%define		theme	black

Summary:	Splashutils - black theme
Summary(pl):	Splashutils - motyw black
Name:		splashutils-theme-%{theme}
Version:	1
Release:	1
License:	GPL v2
Group:		Themes
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	438a012a230ec068bc29c225756999f2
Requires:	splashutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/splash

%description
Black PLD theme for splashutils.

%description -l pl
Motyw PLD black do splashutils.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

THEME_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/%{theme}

install -d $THEME_DIR/images
install %{theme}/*.cfg $THEME_DIR
install %{theme}/images/*.jpg $THEME_DIR/images

ln -sf	%{_sysconfdir}/%{theme}/images/verbose-640x480.jpg \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{theme}/images/silent-640x480.jpg
ln -sf	%{_sysconfdir}/%{theme}/images/verbose-800x600.jpg \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{theme}/images/silent-800x600.jpg
ln -sf	%{_sysconfdir}/%{theme}/images/verbose-1024x768.jpg \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{theme}/images/silent-1024x768.jpg
ln -sf	%{_sysconfdir}/%{theme}/images/verbose-1280x1024.jpg \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{theme}/images/silent-1280x1024.jpg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/%{theme}
