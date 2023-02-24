import QtQuick 2.15
import QtQuick.Controls 2.15

Button{
    id: ctrl

    background: Rectangle {
        implicitWidth: 78
        implicitHeight: 56
        color: ctrl.hovered ? "#50ffffff": "transparent"
    }

    contentItem: Text{
        text: ctrl.text
        font: ctrl.font
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHcenter
        control. ctrl.hovered ? "white" : "transparent"
    }
}