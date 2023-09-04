#!/bin/python3
from material_color_utilities_python import *
from pathlib import Path
import sys


class CorePaletteExtended:
    def __init__(self, argb):
        hct = Hct.fromInt(argb)
        hue = hct.hue
        self.error = TonalPalette.fromHueAndChroma(25, 84)
        self.a1 = TonalPalette.fromHueAndChroma(hue, max(48, hct.chroma))
        self.a2 = TonalPalette.fromHueAndChroma(hue, 16)
        self.a3 = TonalPalette.fromHueAndChroma(hue + 60, 24)
        self.n1 = TonalPalette.fromHueAndChroma(hue, 4)
        self.n2 = TonalPalette.fromHueAndChroma(hue, 8)
        # Rotate hue 30deg...
        self.a1_2 = TonalPalette.fromHueAndChroma(
            hue + 30, max(48, hct.chroma))
        self.a2_2 = TonalPalette.fromHueAndChroma(hue + 45, 16)
        self.n1_2 = TonalPalette.fromHueAndChroma(hue + 45, 4)
        self.n2_2 = TonalPalette.fromHueAndChroma(hue + 45, 8)
        # Rotate hue 60deg...
        self.a1_3 = TonalPalette.fromHueAndChroma(
            hue + 60, max(48, hct.chroma))
        self.a2_3 = TonalPalette.fromHueAndChroma(hue + 90, 16)
        self.n1_3 = TonalPalette.fromHueAndChroma(hue + 90, 4)
        self.n2_3 = TonalPalette.fromHueAndChroma(hue + 90, 8)
        # Rotate hue 90deg...
        self.a1_4 = TonalPalette.fromHueAndChroma(
            hue + 90, max(48, hct.chroma))
        self.a2_4 = TonalPalette.fromHueAndChroma(hue + 135, 16)
        self.n1_4 = TonalPalette.fromHueAndChroma(hue + 135, 4)
        self.n2_4 = TonalPalette.fromHueAndChroma(hue + 135, 8)
        # Rotate hue 120deg...
        self.a1_5 = TonalPalette.fromHueAndChroma(
            hue + 120, max(48, hct.chroma))
        self.a2_5 = TonalPalette.fromHueAndChroma(hue + 180, 16)
        self.n1_5 = TonalPalette.fromHueAndChroma(hue + 180, 4)
        self.n2_5 = TonalPalette.fromHueAndChroma(hue + 180, 8)
        # Rotate hue 150deg...
        self.a1_6 = TonalPalette.fromHueAndChroma(
            hue + 150, max(48, hct.chroma))
        self.a2_6 = TonalPalette.fromHueAndChroma(hue + 225, 16)
        self.n1_6 = TonalPalette.fromHueAndChroma(hue + 225, 4)
        self.n2_6 = TonalPalette.fromHueAndChroma(hue + 225, 8)
        # Rotate hue 180deg...
        self.a1_7 = TonalPalette.fromHueAndChroma(
            hue + 180, max(48, hct.chroma))
        self.a2_7 = TonalPalette.fromHueAndChroma(hue + 270, 16)
        self.n1_7 = TonalPalette.fromHueAndChroma(hue + 270, 4)
        self.n2_7 = TonalPalette.fromHueAndChroma(hue + 270, 8)
        # Rotate hue 210deg...
        self.a1_8 = TonalPalette.fromHueAndChroma(
            hue + 210, max(48, hct.chroma))
        self.a2_8 = TonalPalette.fromHueAndChroma(hue + 315, 16)
        self.n1_8 = TonalPalette.fromHueAndChroma(hue + 315, 4)
        self.n2_8 = TonalPalette.fromHueAndChroma(hue + 315, 8)

    # /**
    #  * @param argb ARGB representation of a color
    #  */

    @staticmethod
    def of(argb):
        return CorePaletteExtended(argb)


class SchemeExtended:
    def __init__(self, props):
        self.props = props

    def get_primary(self):
        return self.props["primary"]

    def get_primaryContainer(self):
        return self.props["primaryContainer"]

    def get_onPrimary(self):
        return self.props["onPrimary"]

    def get_onPrimaryContainer(self):
        return self.props["onPrimaryContainer"]

    def get_secondary(self):
        return self.props["secondary"]

    def get_secondaryContainer(self):
        return self.props["secondaryContainer"]

    def get_onSecondary(self):
        return self.props["onSecondary"]

    def get_onSecondaryContainer(self):
        return self.props["onSecondaryContainer"]

    def get_tertiary(self):
        return self.props["tertiary"]

    def get_onTertiary(self):
        return self.props["onTertiary"]

    def get_tertiaryContainer(self):
        return self.props["tertiaryContainer"]

    def get_onTertiaryContainer(self):
        return self.props["onTertiaryContainer"]

    def get_error(self):
        return self.props["error"]

    def get_onError(self):
        return self.props["onError"]

    def get_errorContainer(self):
        return self.props["errorContainer"]

    def get_onErrorContainer(self):
        return self.props["onErrorContainer"]

    def get_background(self):
        return self.props["background"]

    def get_onBackground(self):
        return self.props["onBackground"]

    def get_surface(self):
        return self.props["surface"]

    def get_onSurface(self):
        return self.props["onSurface"]

    def get_surfaceVariant(self):
        return self.props["surfaceVariant"]

    def get_onSurfaceVariant(self):
        return self.props["onSurfaceVariant"]

    def get_outline(self):
        return self.props["outline"]

    def get_shadow(self):
        return self.props["shadow"]

    def get_inverseSurface(self):
        return self.props["inverseSurface"]

    def get_inverseOnSurface(self):
        return self.props["inverseOnSurface"]

    def get_inversePrimary(self):
        return self.props["inversePrimary"]
    # Rotate hue 30deg...

    def get_primary2(self):
        return self.props["primary2"]

    def get_primaryContainer2(self):
        return self.props["primaryContainer2"]

    def get_onPrimary2(self):
        return self.props["onPrimary2"]

    def get_onPrimaryContainer2(self):
        return self.props["onPrimaryContainer2"]

    def get_secondary2(self):
        return self.props["secondary2"]

    def get_secondaryContainer2(self):
        return self.props["secondaryContainer2"]

    def get_onSecondary2(self):
        return self.props["onSecondary2"]

    def get_onSecondaryContainer2(self):
        return self.props["onSecondaryContainer2"]

    def get_background2(self):
        return self.props["background2"]

    def get_onBackground2(self):
        return self.props["onBackground2"]

    def get_surface2(self):
        return self.props["surface2"]

    def get_onSurface2(self):
        return self.props["onSurface2"]

    def get_surfaceVariant2(self):
        return self.props["surfaceVariant2"]

    def get_onSurfaceVariant2(self):
        return self.props["onSurfaceVariant2"]
    # Rotate hue 60deg...

    def get_primary3(self):
        return self.props["primary3"]

    def get_primaryContainer3(self):
        return self.props["primaryContainer3"]

    def get_onPrimary3(self):
        return self.props["onPrimary3"]

    def get_onPrimaryContainer3(self):
        return self.props["onPrimaryContainer3"]

    def get_secondary3(self):
        return self.props["secondary3"]

    def get_secondaryContainer3(self):
        return self.props["secondaryContainer3"]

    def get_onSecondary3(self):
        return self.props["onSecondary3"]

    def get_onSecondaryContainer3(self):
        return self.props["onSecondaryContainer3"]

    def get_background3(self):
        return self.props["background3"]

    def get_onBackground3(self):
        return self.props["onBackground3"]

    def get_surface3(self):
        return self.props["surface3"]

    def get_onSurface3(self):
        return self.props["onSurface3"]

    def get_surfaceVariant3(self):
        return self.props["surfaceVariant3"]

    def get_onSurfaceVariant3(self):
        return self.props["onSurfaceVariant3"]
    # Rotate hue 90deg...

    def get_primary4(self):
        return self.props["primary4"]

    def get_primaryContainer4(self):
        return self.props["primaryContainer4"]

    def get_onPrimary4(self):
        return self.props["onPrimary4"]

    def get_onPrimaryContainer4(self):
        return self.props["onPrimaryContainer4"]

    def get_secondary4(self):
        return self.props["secondary4"]

    def get_secondaryContainer4(self):
        return self.props["secondaryContainer4"]

    def get_onSecondary4(self):
        return self.props["onSecondary4"]

    def get_onSecondaryContainer4(self):
        return self.props["onSecondaryContainer4"]

    def get_background4(self):
        return self.props["background4"]

    def get_onBackground4(self):
        return self.props["onBackground4"]

    def get_surface4(self):
        return self.props["surface4"]

    def get_onSurface4(self):
        return self.props["onSurface4"]

    def get_surfaceVariant4(self):
        return self.props["surfaceVariant4"]

    def get_onSurfaceVariant4(self):
        return self.props["onSurfaceVariant4"]
    # Rotate hue 120deg...

    def get_primary5(self):
        return self.props["primary5"]

    def get_primaryContainer5(self):
        return self.props["primaryContainer5"]

    def get_onPrimary5(self):
        return self.props["onPrimary5"]

    def get_onPrimaryContainer5(self):
        return self.props["onPrimaryContainer5"]

    def get_secondary5(self):
        return self.props["secondary5"]

    def get_secondaryContainer5(self):
        return self.props["secondaryContainer5"]

    def get_onSecondary5(self):
        return self.props["onSecondary5"]

    def get_onSecondaryContainer5(self):
        return self.props["onSecondaryContainer5"]

    def get_background5(self):
        return self.props["background5"]

    def get_onBackground5(self):
        return self.props["onBackground5"]

    def get_surface5(self):
        return self.props["surface5"]

    def get_onSurface5(self):
        return self.props["onSurface5"]

    def get_surfaceVariant5(self):
        return self.props["surfaceVariant5"]

    def get_onSurfaceVariant5(self):
        return self.props["onSurfaceVariant5"]
    # Rotate hue 150deg...

    def get_primary6(self):
        return self.props["primary6"]

    def get_primaryContainer6(self):
        return self.props["primaryContainer6"]

    def get_onPrimary6(self):
        return self.props["onPrimary6"]

    def get_onPrimaryContainer6(self):
        return self.props["onPrimaryContainer6"]

    def get_secondary6(self):
        return self.props["secondary6"]

    def get_secondaryContainer6(self):
        return self.props["secondaryContainer6"]

    def get_onSecondary6(self):
        return self.props["onSecondary6"]

    def get_onSecondaryContainer6(self):
        return self.props["onSecondaryContainer6"]

    def get_background6(self):
        return self.props["background6"]

    def get_onBackground6(self):
        return self.props["onBackground6"]

    def get_surface6(self):
        return self.props["surface6"]

    def get_onSurface6(self):
        return self.props["onSurface6"]

    def get_surfaceVariant6(self):
        return self.props["surfaceVariant6"]

    def get_onSurfaceVariant6(self):
        return self.props["onSurfaceVariant6"]
    # Rotate hue 180deg...

    def get_primary7(self):
        return self.props["primary7"]

    def get_primaryContainer7(self):
        return self.props["primaryContainer7"]

    def get_onPrimary7(self):
        return self.props["onPrimary7"]

    def get_onPrimaryContainer7(self):
        return self.props["onPrimaryContainer7"]

    def get_secondary7(self):
        return self.props["secondary7"]

    def get_secondaryContainer7(self):
        return self.props["secondaryContainer7"]

    def get_onSecondary7(self):
        return self.props["onSecondary7"]

    def get_onSecondaryContainer7(self):
        return self.props["onSecondaryContainer7"]

    def get_background7(self):
        return self.props["background7"]

    def get_onBackground7(self):
        return self.props["onBackground7"]

    def get_surface7(self):
        return self.props["surface7"]

    def get_onSurface7(self):
        return self.props["onSurface7"]

    def get_surfaceVariant7(self):
        return self.props["surfaceVariant7"]

    def get_onSurfaceVariant7(self):
        return self.props["onSurfaceVariant7"]
    # Rotate hue 210deg...

    def get_primary8(self):
        return self.props["primary8"]

    def get_primaryContainer8(self):
        return self.props["primaryContainer8"]

    def get_onPrimary8(self):
        return self.props["onPrimary8"]

    def get_onPrimaryContainer8(self):
        return self.props["onPrimaryContainer8"]

    def get_secondary8(self):
        return self.props["secondary8"]

    def get_secondaryContainer8(self):
        return self.props["secondaryContainer8"]

    def get_onSecondary8(self):
        return self.props["onSecondary8"]

    def get_onSecondaryContainer8(self):
        return self.props["onSecondaryContainer8"]

    def get_background8(self):
        return self.props["background8"]

    def get_onBackground8(self):
        return self.props["onBackground8"]

    def get_surface8(self):
        return self.props["surface8"]

    def get_onSurface8(self):
        return self.props["onSurface8"]

    def get_surfaceVariant8(self):
        return self.props["surfaceVariant8"]

    def get_onSurfaceVariant8(self):
        return self.props["onSurfaceVariant8"]

    primary = property(get_primary)
    primaryContainer = property(get_primaryContainer)
    onPrimary = property(get_onPrimary)
    onPrimaryContainer = property(get_onPrimaryContainer)
    secondary = property(get_secondary)
    secondaryContainer = property(get_secondaryContainer)
    onSecondary = property(get_onSecondary)
    onSecondaryContainer = property(get_onSecondaryContainer)
    tertiary = property(get_tertiary)
    onTertiary = property(get_onTertiary)
    tertiaryContainer = property(get_tertiaryContainer)
    onTertiaryContainer = property(get_onTertiaryContainer)
    error = property(get_error)
    onError = property(get_onError)
    errorContainer = property(get_errorContainer)
    onErrorContainer = property(get_onErrorContainer)
    background = property(get_background)
    onBackground = property(get_onBackground)
    surface = property(get_surface)
    onSurface = property(get_onSurface)
    surfaceVariant = property(get_surfaceVariant)
    onSurfaceVariant = property(get_onSurfaceVariant)
    outline = property(get_outline)
    shadow = property(get_shadow)
    inverseSurface = property(get_inverseSurface)
    inverseOnSurface = property(get_inverseOnSurface)
    inversePrimary = property(get_inversePrimary)
    # 2
    primary2 = property(get_primary2)
    primaryContainer2 = property(get_primaryContainer2)
    onPrimary2 = property(get_onPrimary2)
    onPrimaryContainer2 = property(get_onPrimaryContainer2)
    secondary2 = property(get_secondary2)
    secondaryContainer2 = property(get_secondaryContainer2)
    onSecondary2 = property(get_onSecondary2)
    onSecondaryContainer2 = property(get_onSecondaryContainer2)
    background2 = property(get_background2)
    onBackground2 = property(get_onBackground2)
    surface2 = property(get_surface2)
    onSurface2 = property(get_onSurface2)
    surfaceVariant2 = property(get_surfaceVariant2)
    onSurfaceVariant2 = property(get_onSurfaceVariant2)
    # 3
    primary3 = property(get_primary3)
    primaryContainer3 = property(get_primaryContainer3)
    onPrimary3 = property(get_onPrimary3)
    onPrimaryContainer3 = property(get_onPrimaryContainer3)
    secondary3 = property(get_secondary3)
    secondaryContainer3 = property(get_secondaryContainer3)
    onSecondary3 = property(get_onSecondary3)
    onSecondaryContainer3 = property(get_onSecondaryContainer3)
    background3 = property(get_background3)
    onBackground3 = property(get_onBackground3)
    surface3 = property(get_surface3)
    onSurface3 = property(get_onSurface3)
    surfaceVariant3 = property(get_surfaceVariant3)
    onSurfaceVariant3 = property(get_onSurfaceVariant3)
    # 4
    primary4 = property(get_primary4)
    primaryContainer4 = property(get_primaryContainer4)
    onPrimary4 = property(get_onPrimary4)
    onPrimaryContainer4 = property(get_onPrimaryContainer4)
    secondary4 = property(get_secondary4)
    secondaryContainer4 = property(get_secondaryContainer4)
    onSecondary4 = property(get_onSecondary4)
    onSecondaryContainer4 = property(get_onSecondaryContainer4)
    background4 = property(get_background4)
    onBackground4 = property(get_onBackground4)
    surface4 = property(get_surface4)
    onSurface4 = property(get_onSurface4)
    surfaceVariant4 = property(get_surfaceVariant4)
    onSurfaceVariant4 = property(get_onSurfaceVariant4)
    # 5
    primary5 = property(get_primary5)
    primaryContainer5 = property(get_primaryContainer5)
    onPrimary5 = property(get_onPrimary5)
    onPrimaryContainer5 = property(get_onPrimaryContainer5)
    secondary5 = property(get_secondary5)
    secondaryContainer5 = property(get_secondaryContainer5)
    onSecondary5 = property(get_onSecondary5)
    onSecondaryContainer5 = property(get_onSecondaryContainer5)
    background5 = property(get_background5)
    onBackground5 = property(get_onBackground5)
    surface5 = property(get_surface5)
    onSurface5 = property(get_onSurface5)
    surfaceVariant5 = property(get_surfaceVariant5)
    onSurfaceVariant5 = property(get_onSurfaceVariant5)
    # 6
    primary6 = property(get_primary6)
    primaryContainer6 = property(get_primaryContainer6)
    onPrimary6 = property(get_onPrimary6)
    onPrimaryContainer6 = property(get_onPrimaryContainer6)
    secondary6 = property(get_secondary6)
    secondaryContainer6 = property(get_secondaryContainer6)
    onSecondary6 = property(get_onSecondary6)
    onSecondaryContainer6 = property(get_onSecondaryContainer6)
    background6 = property(get_background6)
    onBackground6 = property(get_onBackground6)
    surface6 = property(get_surface6)
    onSurface6 = property(get_onSurface6)
    surfaceVariant6 = property(get_surfaceVariant6)
    onSurfaceVariant6 = property(get_onSurfaceVariant6)
    # 7
    primary7 = property(get_primary7)
    primaryContainer7 = property(get_primaryContainer7)
    onPrimary7 = property(get_onPrimary7)
    onPrimaryContainer7 = property(get_onPrimaryContainer7)
    secondary7 = property(get_secondary7)
    secondaryContainer7 = property(get_secondaryContainer7)
    onSecondary7 = property(get_onSecondary7)
    onSecondaryContainer7 = property(get_onSecondaryContainer7)
    background7 = property(get_background7)
    onBackground7 = property(get_onBackground7)
    surface7 = property(get_surface7)
    onSurface7 = property(get_onSurface7)
    surfaceVariant7 = property(get_surfaceVariant7)
    onSurfaceVariant7 = property(get_onSurfaceVariant7)
    # 8
    primary8 = property(get_primary8)
    primaryContainer8 = property(get_primaryContainer8)
    onPrimary8 = property(get_onPrimary8)
    onPrimaryContainer8 = property(get_onPrimaryContainer8)
    secondary8 = property(get_secondary8)
    secondaryContainer8 = property(get_secondaryContainer8)
    onSecondary8 = property(get_onSecondary8)
    onSecondaryContainer8 = property(get_onSecondaryContainer8)
    background8 = property(get_background8)
    onBackground8 = property(get_onBackground8)
    surface8 = property(get_surface8)
    onSurface8 = property(get_onSurface8)
    surfaceVariant8 = property(get_surfaceVariant8)
    onSurfaceVariant8 = property(get_onSurfaceVariant8)

    # /**
    #  * @param argb ARGB representation of a color.
    #  * @return Light Material color scheme, based on the color's hue.
    #  */
    @staticmethod
    def light(argb):
        core = CorePaletteExtended.of(argb)
        return SchemeExtended({
            "primary": core.a1.tone(40),
            "onPrimary": core.a1.tone(100),
            "primaryContainer": core.a1.tone(90),
            "onPrimaryContainer": core.a1.tone(10),
            "secondary": core.a2.tone(40),
            "onSecondary": core.a2.tone(100),
            "secondaryContainer": core.a2.tone(90),
            "onSecondaryContainer": core.a2.tone(10),
            "tertiary": core.a3.tone(40),
            "onTertiary": core.a3.tone(100),
            "tertiaryContainer": core.a3.tone(90),
            "onTertiaryContainer": core.a3.tone(10),
            "error": core.error.tone(40),
            "onError": core.error.tone(100),
            "errorContainer": core.error.tone(90),
            "onErrorContainer": core.error.tone(10),
            "background": core.n1.tone(99),
            "onBackground": core.n1.tone(10),
            "surface": core.n1.tone(99),
            "onSurface": core.n1.tone(10),
            "surfaceVariant": core.n2.tone(90),
            "onSurfaceVariant": core.n2.tone(30),
            "outline": core.n2.tone(50),
            "shadow": core.n1.tone(0),
            "inverseSurface": core.n1.tone(20),
            "inverseOnSurface": core.n1.tone(95),
            "inversePrimary": core.a1.tone(80),
            # 2
            "primary2": core.a1_2.tone(40),
            "onPrimary2": core.a1_2.tone(100),
            "primaryContainer2": core.a1_2.tone(90),
            "onPrimaryContainer2": core.a1_2.tone(10),
            "secondary2": core.a2_2.tone(40),
            "onSecondary2": core.a2_2.tone(100),
            "secondaryContainer2": core.a2_2.tone(90),
            "onSecondaryContainer2": core.a2_2.tone(10),
            "background2": core.n1_2.tone(99),
            "onBackground2": core.n1_2.tone(10),
            "surface2": core.n1_2.tone(99),
            "onSurface2": core.n1_2.tone(10),
            "surfaceVariant2": core.n2_2.tone(90),
            "onSurfaceVariant2": core.n2_2.tone(30),
            # 3
            "primary3": core.a1_3.tone(40),
            "onPrimary3": core.a1_3.tone(100),
            "primaryContainer3": core.a1_3.tone(90),
            "onPrimaryContainer3": core.a1_3.tone(10),
            "secondary3": core.a2_3.tone(40),
            "onSecondary3": core.a2_3.tone(100),
            "secondaryContainer3": core.a2_3.tone(90),
            "onSecondaryContainer3": core.a2_3.tone(10),
            "background3": core.n1_3.tone(99),
            "onBackground3": core.n1_3.tone(10),
            "surface3": core.n1_3.tone(99),
            "onSurface3": core.n1_3.tone(10),
            "surfaceVariant3": core.n2_3.tone(90),
            "onSurfaceVariant3": core.n2_3.tone(30),
            # 4
            "primary4": core.a1_4.tone(40),
            "onPrimary4": core.a1_4.tone(100),
            "primaryContainer4": core.a1_4.tone(90),
            "onPrimaryContainer4": core.a1_4.tone(10),
            "secondary4": core.a2_4.tone(40),
            "onSecondary4": core.a2_4.tone(100),
            "secondaryContainer4": core.a2_4.tone(90),
            "onSecondaryContainer4": core.a2_4.tone(10),
            "background4": core.n1_4.tone(99),
            "onBackground4": core.n1_4.tone(10),
            "surface4": core.n1_4.tone(99),
            "onSurface4": core.n1_4.tone(10),
            "surfaceVariant4": core.n2_4.tone(90),
            "onSurfaceVariant4": core.n2_4.tone(30),
            # 5
            "primary5": core.a1_5.tone(40),
            "onPrimary5": core.a1_5.tone(100),
            "primaryContainer5": core.a1_5.tone(90),
            "onPrimaryContainer5": core.a1_5.tone(10),
            "secondary5": core.a2_5.tone(40),
            "onSecondary5": core.a2_5.tone(100),
            "secondaryContainer5": core.a2_5.tone(90),
            "onSecondaryContainer5": core.a2_5.tone(10),
            "background5": core.n1_5.tone(99),
            "onBackground5": core.n1_5.tone(10),
            "surface5": core.n1_5.tone(99),
            "onSurface5": core.n1_5.tone(10),
            "surfaceVariant5": core.n2_5.tone(90),
            "onSurfaceVariant5": core.n2_5.tone(30),
            # 6
            "primary6": core.a1_6.tone(40),
            "onPrimary6": core.a1_6.tone(100),
            "primaryContainer6": core.a1_6.tone(90),
            "onPrimaryContainer6": core.a1_6.tone(10),
            "secondary6": core.a2_6.tone(40),
            "onSecondary6": core.a2_6.tone(100),
            "secondaryContainer6": core.a2_6.tone(90),
            "onSecondaryContainer6": core.a2_6.tone(10),
            "background6": core.n1_6.tone(99),
            "onBackground6": core.n1_6.tone(10),
            "surface6": core.n1_6.tone(99),
            "onSurface6": core.n1_6.tone(10),
            "surfaceVariant6": core.n2_6.tone(90),
            "onSurfaceVariant6": core.n2_6.tone(30),
            # 7
            "primary7": core.a1_7.tone(40),
            "onPrimary7": core.a1_7.tone(100),
            "primaryContainer7": core.a1_7.tone(90),
            "onPrimaryContainer7": core.a1_7.tone(10),
            "secondary7": core.a2_7.tone(40),
            "onSecondary7": core.a2_7.tone(100),
            "secondaryContainer7": core.a2_7.tone(90),
            "onSecondaryContainer7": core.a2_7.tone(10),
            "background7": core.n1_7.tone(99),
            "onBackground7": core.n1_7.tone(10),
            "surface7": core.n1_7.tone(99),
            "onSurface7": core.n1_7.tone(10),
            "surfaceVariant7": core.n2_7.tone(90),
            "onSurfaceVariant7": core.n2_7.tone(30),
            # 8
            "primary8": core.a1_8.tone(40),
            "onPrimary8": core.a1_8.tone(100),
            "primaryContainer8": core.a1_8.tone(90),
            "onPrimaryContainer8": core.a1_8.tone(10),
            "secondary8": core.a2_8.tone(40),
            "onSecondary8": core.a2_8.tone(100),
            "secondaryContainer8": core.a2_8.tone(90),
            "onSecondaryContainer8": core.a2_8.tone(10),
            "background8": core.n1_8.tone(99),
            "onBackground8": core.n1_8.tone(10),
            "surface8": core.n1_8.tone(99),
            "onSurface8": core.n1_8.tone(10),
            "surfaceVariant8": core.n2_8.tone(90),
            "onSurfaceVariant8": core.n2_8.tone(30),

        })

    # /**
    #  * @param argb ARGB representation of a color.
    #  * @return Dark Material color scheme, based on the color's hue.
    #  */
    @staticmethod
    def dark(argb):
        core = CorePaletteExtended.of(argb)
        return SchemeExtended({
            "primary": core.a1.tone(80),
            "onPrimary": core.a1.tone(20),
            "primaryContainer": core.a1.tone(30),
            "onPrimaryContainer": core.a1.tone(90),
            "secondary": core.a2.tone(80),
            "onSecondary": core.a2.tone(20),
            "secondaryContainer": core.a2.tone(30),
            "onSecondaryContainer": core.a2.tone(90),
            "tertiary": core.a3.tone(80),
            "onTertiary": core.a3.tone(20),
            "tertiaryContainer": core.a3.tone(30),
            "onTertiaryContainer": core.a3.tone(90),
            "error": core.error.tone(80),
            "onError": core.error.tone(20),
            "errorContainer": core.error.tone(30),
            "onErrorContainer": core.error.tone(80),
            "background": core.n1.tone(10),
            "onBackground": core.n1.tone(90),
            "surface": core.n1.tone(10),
            "onSurface": core.n1.tone(90),
            "surfaceVariant": core.n2.tone(30),
            "onSurfaceVariant": core.n2.tone(80),
            "outline": core.n2.tone(60),
            "shadow": core.n1.tone(0),
            "inverseSurface": core.n1.tone(90),
            "inverseOnSurface": core.n1.tone(20),
            "inversePrimary": core.a1.tone(40),
            # 2
            "primary2": core.a1_2.tone(80),
            "onPrimary2": core.a1_2.tone(20),
            "primaryContainer2": core.a1_2.tone(30),
            "onPrimaryContainer2": core.a1_2.tone(90),
            "secondary2": core.a2_2.tone(80),
            "onSecondary2": core.a2_2.tone(20),
            "secondaryContainer2": core.a2_2.tone(30),
            "onSecondaryContainer2": core.a2_2.tone(90),
            "background2": core.n1_2.tone(10),
            "onBackground2": core.n1_2.tone(90),
            "surface2": core.n1_2.tone(10),
            "onSurface2": core.n1_2.tone(90),
            "surfaceVariant2": core.n2_2.tone(30),
            "onSurfaceVariant2": core.n2_2.tone(80),
            # 3
            "primary3": core.a1_3.tone(80),
            "onPrimary3": core.a1_3.tone(20),
            "primaryContainer3": core.a1_3.tone(30),
            "onPrimaryContainer3": core.a1_3.tone(90),
            "secondary3": core.a2_3.tone(80),
            "onSecondary3": core.a2_3.tone(20),
            "secondaryContainer3": core.a2_3.tone(30),
            "onSecondaryContainer3": core.a2_3.tone(90),
            "background3": core.n1_3.tone(10),
            "onBackground3": core.n1_3.tone(90),
            "surface3": core.n1_3.tone(10),
            "onSurface3": core.n1_3.tone(90),
            "surfaceVariant3": core.n2_3.tone(30),
            "onSurfaceVariant3": core.n2_3.tone(80),
            # 4
            "primary4": core.a1_4.tone(80),
            "onPrimary4": core.a1_4.tone(20),
            "primaryContainer4": core.a1_4.tone(30),
            "onPrimaryContainer4": core.a1_4.tone(90),
            "secondary4": core.a2_4.tone(80),
            "onSecondary4": core.a2_4.tone(20),
            "secondaryContainer4": core.a2_4.tone(30),
            "onSecondaryContainer4": core.a2_4.tone(90),
            "background4": core.n1_4.tone(10),
            "onBackground4": core.n1_4.tone(90),
            "surface4": core.n1_4.tone(10),
            "onSurface4": core.n1_4.tone(90),
            "surfaceVariant4": core.n2_4.tone(30),
            "onSurfaceVariant4": core.n2_4.tone(80),
            # 5
            "primary5": core.a1_5.tone(80),
            "onPrimary5": core.a1_5.tone(20),
            "primaryContainer5": core.a1_5.tone(30),
            "onPrimaryContainer5": core.a1_5.tone(90),
            "secondary5": core.a2_5.tone(80),
            "onSecondary5": core.a2_5.tone(20),
            "secondaryContainer5": core.a2_5.tone(30),
            "onSecondaryContainer5": core.a2_5.tone(90),
            "background5": core.n1_5.tone(10),
            "onBackground5": core.n1_5.tone(90),
            "surface5": core.n1_5.tone(10),
            "onSurface5": core.n1_5.tone(90),
            "surfaceVariant5": core.n2_5.tone(30),
            "onSurfaceVariant5": core.n2_5.tone(80),
            # 6
            "primary6": core.a1_6.tone(80),
            "onPrimary6": core.a1_6.tone(20),
            "primaryContainer6": core.a1_6.tone(30),
            "onPrimaryContainer6": core.a1_6.tone(90),
            "secondary6": core.a2_6.tone(80),
            "onSecondary6": core.a2_6.tone(20),
            "secondaryContainer6": core.a2_6.tone(30),
            "onSecondaryContainer6": core.a2_6.tone(90),
            "background6": core.n1_6.tone(10),
            "onBackground6": core.n1_6.tone(90),
            "surface6": core.n1_6.tone(10),
            "onSurface6": core.n1_6.tone(90),
            "surfaceVariant6": core.n2_6.tone(30),
            "onSurfaceVariant6": core.n2_6.tone(80),
            # 7
            "primary7": core.a1_7.tone(80),
            "onPrimary7": core.a1_7.tone(20),
            "primaryContainer7": core.a1_7.tone(30),
            "onPrimaryContainer7": core.a1_7.tone(90),
            "secondary7": core.a2_7.tone(80),
            "onSecondary7": core.a2_7.tone(20),
            "secondaryContainer7": core.a2_7.tone(30),
            "onSecondaryContainer7": core.a2_7.tone(90),
            "background7": core.n1_7.tone(10),
            "onBackground7": core.n1_7.tone(90),
            "surface7": core.n1_7.tone(10),
            "onSurface7": core.n1_7.tone(90),
            "surfaceVariant7": core.n2_7.tone(30),
            "onSurfaceVariant7": core.n2_7.tone(80),
            # 8
            "primary8": core.a1_8.tone(80),
            "onPrimary8": core.a1_8.tone(20),
            "primaryContainer8": core.a1_8.tone(30),
            "onPrimaryContainer8": core.a1_8.tone(90),
            "secondary8": core.a2_8.tone(80),
            "onSecondary8": core.a2_8.tone(20),
            "secondaryContainer8": core.a2_8.tone(30),
            "onSecondaryContainer8": core.a2_8.tone(90),
            "background8": core.n1_8.tone(10),
            "onBackground8": core.n1_8.tone(90),
            "surface8": core.n1_8.tone(10),
            "onSurface8": core.n1_8.tone(90),
            "surfaceVariant8": core.n2_8.tone(30),
            "onSurfaceVariant8": core.n2_8.tone(80),
        })

    def toJSON(self):
        return json.dumps(self.props)


def themeFromSauceColor(source, customColors=[]):  # Sauce so it doesn't conflict
    palette = CorePaletteExtended.of(source)
    return {
        "source": source,
        "schemes": {
            "light": SchemeExtended.light(source),
            "dark": SchemeExtended.dark(source),
        },
        "palettes": {
            "primary": palette.a1,
            "secondary": palette.a2,
            "tertiary": palette.a3,
            "neutral": palette.n1,
            "neutralVariant": palette.n2,
            "error": palette.error,
        },
        "customColors": [customColor(source, c) for c in customColors]
    }


img = 0
newtheme = 0
if len(sys.argv) > 1 and (sys.argv[1] == '--path' or sys.argv[1] == '--image'):
    img = Image.open(sys.argv[2])
    basewidth = 64
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    newtheme = themeFromSauceColor(sourceColorFromImage(img))
elif len(sys.argv) > 1 and sys.argv[1] == '--color':
    colorstr = sys.argv[2]
    newtheme = themeFromSauceColor(argbFromHex(colorstr))
else:
    img = Image.open(str(Path.home())+'/.config/ags/scripts/tmp/wallpaper')
    basewidth = 64
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    newtheme = themeFromSauceColor(sourceColorFromImage(img))

colorscheme = 0
if ("-l" in sys.argv):
    colorscheme = newtheme['schemes']['light']
else:
    colorscheme = newtheme['schemes']['dark']

primary = hexFromArgb(colorscheme.primary)
onPrimary = hexFromArgb(colorscheme.onPrimary)
primaryContainer = hexFromArgb(colorscheme.primaryContainer)
onPrimaryContainer = hexFromArgb(colorscheme.onPrimaryContainer)
secondary = hexFromArgb(colorscheme.secondary)
onSecondary = hexFromArgb(colorscheme.onSecondary)
secondaryContainer = hexFromArgb(colorscheme.secondaryContainer)
onSecondaryContainer = hexFromArgb(colorscheme.onSecondaryContainer)
tertiary = hexFromArgb(colorscheme.tertiary)
onTertiary = hexFromArgb(colorscheme.onTertiary)
tertiaryContainer = hexFromArgb(colorscheme.tertiaryContainer)
onTertiaryContainer = hexFromArgb(colorscheme.onTertiaryContainer)
error = hexFromArgb(colorscheme.error)
onError = hexFromArgb(colorscheme.onError)
errorContainer = hexFromArgb(colorscheme.errorContainer)
onErrorContainer = hexFromArgb(colorscheme.onErrorContainer)
background = hexFromArgb(colorscheme.background)
onBackground = hexFromArgb(colorscheme.onBackground)
surface = hexFromArgb(colorscheme.surface)
onSurface = hexFromArgb(colorscheme.onSurface)
surfaceVariant = hexFromArgb(colorscheme.surfaceVariant)
onSurfaceVariant = hexFromArgb(colorscheme.onSurfaceVariant)
outline = hexFromArgb(colorscheme.outline)
shadow = hexFromArgb(colorscheme.shadow)
inverseSurface = hexFromArgb(colorscheme.inverseSurface)
inverseOnSurface = hexFromArgb(colorscheme.inverseOnSurface)
inversePrimary = hexFromArgb(colorscheme.inversePrimary)
# 2
primary2 = hexFromArgb(colorscheme.primary2)
onPrimary2 = hexFromArgb(colorscheme.onPrimary2)
primaryContainer2 = hexFromArgb(colorscheme.primaryContainer2)
onPrimaryContainer2 = hexFromArgb(colorscheme.onPrimaryContainer2)
secondary2 = hexFromArgb(colorscheme.secondary2)
onSecondary2 = hexFromArgb(colorscheme.onSecondary2)
secondaryContainer2 = hexFromArgb(colorscheme.secondaryContainer2)
onSecondaryContainer2 = hexFromArgb(colorscheme.onSecondaryContainer2)
background2 = hexFromArgb(colorscheme.background2)
onBackground2 = hexFromArgb(colorscheme.onBackground2)
surface2 = hexFromArgb(colorscheme.surface2)
onSurface2 = hexFromArgb(colorscheme.onSurface2)
surfaceVariant2 = hexFromArgb(colorscheme.surfaceVariant2)
onSurfaceVariant2 = hexFromArgb(colorscheme.onSurfaceVariant2)
# 3
primary3 = hexFromArgb(colorscheme.primary3)
onPrimary3 = hexFromArgb(colorscheme.onPrimary3)
primaryContainer3 = hexFromArgb(colorscheme.primaryContainer3)
onPrimaryContainer3 = hexFromArgb(colorscheme.onPrimaryContainer3)
secondary3 = hexFromArgb(colorscheme.secondary3)
onSecondary3 = hexFromArgb(colorscheme.onSecondary3)
secondaryContainer3 = hexFromArgb(colorscheme.secondaryContainer3)
onSecondaryContainer3 = hexFromArgb(colorscheme.onSecondaryContainer3)
background3 = hexFromArgb(colorscheme.background3)
onBackground3 = hexFromArgb(colorscheme.onBackground3)
surface3 = hexFromArgb(colorscheme.surface3)
onSurface3 = hexFromArgb(colorscheme.onSurface3)
surfaceVariant3 = hexFromArgb(colorscheme.surfaceVariant3)
onSurfaceVariant3 = hexFromArgb(colorscheme.onSurfaceVariant3)
# 4
primary4 = hexFromArgb(colorscheme.primary4)
onPrimary4 = hexFromArgb(colorscheme.onPrimary4)
primaryContainer4 = hexFromArgb(colorscheme.primaryContainer4)
onPrimaryContainer4 = hexFromArgb(colorscheme.onPrimaryContainer4)
secondary4 = hexFromArgb(colorscheme.secondary4)
onSecondary4 = hexFromArgb(colorscheme.onSecondary4)
secondaryContainer4 = hexFromArgb(colorscheme.secondaryContainer4)
onSecondaryContainer4 = hexFromArgb(colorscheme.onSecondaryContainer4)
background4 = hexFromArgb(colorscheme.background4)
onBackground4 = hexFromArgb(colorscheme.onBackground4)
surface4 = hexFromArgb(colorscheme.surface4)
onSurface4 = hexFromArgb(colorscheme.onSurface4)
surfaceVariant4 = hexFromArgb(colorscheme.surfaceVariant4)
onSurfaceVariant4 = hexFromArgb(colorscheme.onSurfaceVariant4)
# 5
primary5 = hexFromArgb(colorscheme.primary5)
onPrimary5 = hexFromArgb(colorscheme.onPrimary5)
primaryContainer5 = hexFromArgb(colorscheme.primaryContainer5)
onPrimaryContainer5 = hexFromArgb(colorscheme.onPrimaryContainer5)
secondary5 = hexFromArgb(colorscheme.secondary5)
onSecondary5 = hexFromArgb(colorscheme.onSecondary5)
secondaryContainer5 = hexFromArgb(colorscheme.secondaryContainer5)
onSecondaryContainer5 = hexFromArgb(colorscheme.onSecondaryContainer5)
background5 = hexFromArgb(colorscheme.background5)
onBackground5 = hexFromArgb(colorscheme.onBackground5)
surface5 = hexFromArgb(colorscheme.surface5)
onSurface5 = hexFromArgb(colorscheme.onSurface5)
surfaceVariant5 = hexFromArgb(colorscheme.surfaceVariant5)
onSurfaceVariant5 = hexFromArgb(colorscheme.onSurfaceVariant5)
# 6
primary6 = hexFromArgb(colorscheme.primary6)
onPrimary6 = hexFromArgb(colorscheme.onPrimary6)
primaryContainer6 = hexFromArgb(colorscheme.primaryContainer6)
onPrimaryContainer6 = hexFromArgb(colorscheme.onPrimaryContainer6)
secondary6 = hexFromArgb(colorscheme.secondary6)
onSecondary6 = hexFromArgb(colorscheme.onSecondary6)
secondaryContainer6 = hexFromArgb(colorscheme.secondaryContainer6)
onSecondaryContainer6 = hexFromArgb(colorscheme.onSecondaryContainer6)
background6 = hexFromArgb(colorscheme.background6)
onBackground6 = hexFromArgb(colorscheme.onBackground6)
surface6 = hexFromArgb(colorscheme.surface6)
onSurface6 = hexFromArgb(colorscheme.onSurface6)
surfaceVariant6 = hexFromArgb(colorscheme.surfaceVariant6)
onSurfaceVariant6 = hexFromArgb(colorscheme.onSurfaceVariant6)
# 7
primary7 = hexFromArgb(colorscheme.primary7)
onPrimary7 = hexFromArgb(colorscheme.onPrimary7)
primaryContainer7 = hexFromArgb(colorscheme.primaryContainer7)
onPrimaryContainer7 = hexFromArgb(colorscheme.onPrimaryContainer7)
secondary7 = hexFromArgb(colorscheme.secondary7)
onSecondary7 = hexFromArgb(colorscheme.onSecondary7)
secondaryContainer7 = hexFromArgb(colorscheme.secondaryContainer7)
onSecondaryContainer7 = hexFromArgb(colorscheme.onSecondaryContainer7)
background7 = hexFromArgb(colorscheme.background7)
onBackground7 = hexFromArgb(colorscheme.onBackground7)
surface7 = hexFromArgb(colorscheme.surface7)
onSurface7 = hexFromArgb(colorscheme.onSurface7)
surfaceVariant7 = hexFromArgb(colorscheme.surfaceVariant7)
onSurfaceVariant7 = hexFromArgb(colorscheme.onSurfaceVariant7)
# 8
primary8 = hexFromArgb(colorscheme.primary8)
onPrimary8 = hexFromArgb(colorscheme.onPrimary8)
primaryContainer8 = hexFromArgb(colorscheme.primaryContainer8)
onPrimaryContainer8 = hexFromArgb(colorscheme.onPrimaryContainer8)
secondary8 = hexFromArgb(colorscheme.secondary8)
onSecondary8 = hexFromArgb(colorscheme.onSecondary8)
secondaryContainer8 = hexFromArgb(colorscheme.secondaryContainer8)
onSecondaryContainer8 = hexFromArgb(colorscheme.onSecondaryContainer8)
background8 = hexFromArgb(colorscheme.background8)
onBackground8 = hexFromArgb(colorscheme.onBackground8)
surface8 = hexFromArgb(colorscheme.surface8)
onSurface8 = hexFromArgb(colorscheme.onSurface8)
surfaceVariant8 = hexFromArgb(colorscheme.surfaceVariant8)
onSurfaceVariant8 = hexFromArgb(colorscheme.onSurfaceVariant8)



print('$primary: ' + primary + ';')
print('$onPrimary: ' + onPrimary + ';')
print('$primaryContainer: ' + primaryContainer + ';')
print('$onPrimaryContainer: ' + onPrimaryContainer + ';')
print('$secondary: ' + secondary + ';')
print('$onSecondary: ' + onSecondary + ';')
print('$secondaryContainer: ' + secondaryContainer + ';')
print('$onSecondaryContainer: ' + onSecondaryContainer + ';')
print('$tertiary: ' + tertiary + ';')
print('$onTertiary: ' + onTertiary + ';')
print('$tertiaryContainer: ' + tertiaryContainer + ';')
print('$onTertiaryContainer: ' + onTertiaryContainer + ';')
print('$error: ' + error + ';')
print('$onError: ' + onError + ';')
print('$errorContainer: ' + errorContainer + ';')
print('$onErrorContainer: ' + onErrorContainer + ';')
print('$background: ' + background + ';')
print('$onBackground: ' + onBackground + ';')
print('$surface: ' + surface + ';')
print('$onSurface: ' + onSurface + ';')
print('$surfaceVariant: ' + surfaceVariant + ';')
print('$onSurfaceVariant: ' + onSurfaceVariant + ';')
print('$outline: ' + outline + ';')
print('$shadow: ' + shadow + ';')
print('$inverseSurface: ' + inverseSurface + ';')
print('$inverseOnSurface: ' + inverseOnSurface + ';')
print('$inversePrimary: ' + inversePrimary + ';')
# 2
print('$primary2: ' + primary2 + ';')
print('$onPrimary2: ' + onPrimary2 + ';')
print('$primaryContainer2: ' + primaryContainer2 + ';')
print('$onPrimaryContainer2: ' + onPrimaryContainer2 + ';')
print('$secondary2: ' + secondary2 + ';')
print('$onSecondary2: ' + onSecondary2 + ';')
print('$secondaryContainer2: ' + secondaryContainer2 + ';')
print('$onSecondaryContainer2: ' + onSecondaryContainer2 + ';')
print('$background2: ' + background2 + ';')
print('$onBackground2: ' + onBackground2 + ';')
print('$surface2: ' + surface2 + ';')
print('$onSurface2: ' + onSurface2 + ';')
print('$surfaceVariant2: ' + surfaceVariant2 + ';')
print('$onSurfaceVariant2: ' + onSurfaceVariant2 + ';')
# 3
print('$primary3: ' + primary3 + ';')
print('$onPrimary3: ' + onPrimary3 + ';')
print('$primaryContainer3: ' + primaryContainer3 + ';')
print('$onPrimaryContainer3: ' + onPrimaryContainer3 + ';')
print('$secondary3: ' + secondary3 + ';')
print('$onSecondary3: ' + onSecondary3 + ';')
print('$secondaryContainer3: ' + secondaryContainer3 + ';')
print('$onSecondaryContainer3: ' + onSecondaryContainer3 + ';')
print('$background3: ' + background3 + ';')
print('$onBackground3: ' + onBackground3 + ';')
print('$surface3: ' + surface3 + ';')
print('$onSurface3: ' + onSurface3 + ';')
print('$surfaceVariant3: ' + surfaceVariant3 + ';')
print('$onSurfaceVariant3: ' + onSurfaceVariant3 + ';')
# 4
print('$primary4: ' + primary4 + ';')
print('$onPrimary4: ' + onPrimary4 + ';')
print('$primaryContainer4: ' + primaryContainer4 + ';')
print('$onPrimaryContainer4: ' + onPrimaryContainer4 + ';')
print('$secondary4: ' + secondary4 + ';')
print('$onSecondary4: ' + onSecondary4 + ';')
print('$secondaryContainer4: ' + secondaryContainer4 + ';')
print('$onSecondaryContainer4: ' + onSecondaryContainer4 + ';')
print('$background4: ' + background4 + ';')
print('$onBackground4: ' + onBackground4 + ';')
print('$surface4: ' + surface4 + ';')
print('$onSurface4: ' + onSurface4 + ';')
print('$surfaceVariant4: ' + surfaceVariant4 + ';')
print('$onSurfaceVariant4: ' + onSurfaceVariant4 + ';')
# 5
print('$primary5: ' + primary5 + ';')
print('$onPrimary5: ' + onPrimary5 + ';')
print('$primaryContainer5: ' + primaryContainer5 + ';')
print('$onPrimaryContainer5: ' + onPrimaryContainer5 + ';')
print('$secondary5: ' + secondary5 + ';')
print('$onSecondary5: ' + onSecondary5 + ';')
print('$secondaryContainer5: ' + secondaryContainer5 + ';')
print('$onSecondaryContainer5: ' + onSecondaryContainer5 + ';')
print('$background5: ' + background5 + ';')
print('$onBackground5: ' + onBackground5 + ';')
print('$surface5: ' + surface5 + ';')
print('$onSurface5: ' + onSurface5 + ';')
print('$surfaceVariant5: ' + surfaceVariant5 + ';')
print('$onSurfaceVariant5: ' + onSurfaceVariant5 + ';')
# 6
print('$primary6: ' + primary6 + ';')
print('$onPrimary6: ' + onPrimary6 + ';')
print('$primaryContainer6: ' + primaryContainer6 + ';')
print('$onPrimaryContainer6: ' + onPrimaryContainer6 + ';')
print('$secondary6: ' + secondary6 + ';')
print('$onSecondary6: ' + onSecondary6 + ';')
print('$secondaryContainer6: ' + secondaryContainer6 + ';')
print('$onSecondaryContainer6: ' + onSecondaryContainer6 + ';')
print('$background6: ' + background6 + ';')
print('$onBackground6: ' + onBackground6 + ';')
print('$surface6: ' + surface6 + ';')
print('$onSurface6: ' + onSurface6 + ';')
print('$surfaceVariant6: ' + surfaceVariant6 + ';')
print('$onSurfaceVariant6: ' + onSurfaceVariant6 + ';')
# 7
print('$primary7: ' + primary7 + ';')
print('$onPrimary7: ' + onPrimary7 + ';')
print('$primaryContainer7: ' + primaryContainer7 + ';')
print('$onPrimaryContainer7: ' + onPrimaryContainer7 + ';')
print('$secondary7: ' + secondary7 + ';')
print('$onSecondary7: ' + onSecondary7 + ';')
print('$secondaryContainer7: ' + secondaryContainer7 + ';')
print('$onSecondaryContainer7: ' + onSecondaryContainer7 + ';')
print('$background7: ' + background7 + ';')
print('$onBackground7: ' + onBackground7 + ';')
print('$surface7: ' + surface7 + ';')
print('$onSurface7: ' + onSurface7 + ';')
print('$surfaceVariant7: ' + surfaceVariant7 + ';')
print('$onSurfaceVariant7: ' + onSurfaceVariant7 + ';')
# 8
print('$primary8: ' + primary8 + ';')
print('$onPrimary8: ' + onPrimary8 + ';')
print('$primaryContainer8: ' + primaryContainer8 + ';')
print('$onPrimaryContainer8: ' + onPrimaryContainer8 + ';')
print('$secondary8: ' + secondary8 + ';')
print('$onSecondary8: ' + onSecondary8 + ';')
print('$secondaryContainer8: ' + secondaryContainer8 + ';')
print('$onSecondaryContainer8: ' + onSecondaryContainer8 + ';')
print('$background8: ' + background8 + ';')
print('$onBackground8: ' + onBackground8 + ';')
print('$surface8: ' + surface8 + ';')
print('$onSurface8: ' + onSurface8 + ';')
print('$surfaceVariant8: ' + surfaceVariant8 + ';')
print('$onSurfaceVariant8: ' + onSurfaceVariant8 + ';')
