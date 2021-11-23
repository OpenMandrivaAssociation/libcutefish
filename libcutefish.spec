Name:           libcutefish
Version:        0.5
Release:        1
Summary:        Cutefish System library
License:        GPL-3.0-or-later
Group:          Development/Libraries/Other
URL:            https://github.com/cutefishos/libcutefish
Source:         https://github.com/cutefishos/libcutefish/archive/%{version/}%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  cmake(KF5BluezQt)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5ModemManagerQt)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5Screen)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(ECM)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Sensors)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)

%description
Cutefish desktop interface library, based on QQC2.

%prep
%autosetup

%build
%cmake
%make_build

%install
%make_install -C build

%files
