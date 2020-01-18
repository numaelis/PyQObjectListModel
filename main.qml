import QtQuick 2.4
import QtQuick.Window 2.2

Window {
    visible: true
    height: 300
    width: 200

    Component {
        id: highlightItem
        Rectangle {
            width: parent.width;
            height: 25
            color: "lightsteelblue"; radius: 5
        }
    }

    Component{
        id: listDelegate
        Item{
            id: wrapper
            height: 25
            width: parent.width

            MouseArea {
                anchors.fill: parent
                onClicked: wrapper.ListView.view.currentIndex = index
            }
            Text {
                id: name
                x: parent.x + 5
                anchors.bottom: parent.bottom
                anchors.top: parent.top
                font.pixelSize: 18
                text: object.name +  "    " + object.color
            }
        }
    }

    ListView{
        id: listView1
        anchors.fill: parent
        model: ObjectListModel
        focus: true
        highlight: highlightItem
        highlightFollowsCurrentItem: true
        highlightMoveDuration: 100
        delegate: listDelegate

        onCurrentIndexChanged: {
            console.log(currentIndex)
            console.log(ObjectListModel.get(currentIndex))
        }
    }
}
