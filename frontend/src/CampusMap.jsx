import { MapContainer, TileLayer, GeoJSON, Marker, Popup } from "react-leaflet";
import { useEffect, useState } from "react";
import "leaflet/dist/leaflet.css";

function CampusMap() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/map/full/")
      .then(res => res.json())
      .then(setData)
      .catch(err => console.error(err));
  }, []);

  if (!data) return <p>Loading map...</p>;

  return (
    <MapContainer
      center={[39.12, -76.5]}   // 🔁 replace with your campus center
      zoom={16}
      style={{ height: "100vh", width: "100%" }}
    >
      {/* 🌍 Base Map */}
      <TileLayer
        attribution='&copy; OpenStreetMap contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      {/* 🏫 University Boundary */}
      {data.universities.map(u => (
        <GeoJSON
          key={u.id}
          data={u.boundary}
          style={{
            color: "blue",
            weight: 2,
            fillOpacity: 0.1,
          }}
        />
      ))}

      {/* 🛣 Pathways */}
      {data.pathways.map(p => (
        <GeoJSON
          key={p.id}
          data={p.path}
          style={{
            color: "black",
            weight: 3,
          }}
        />
      ))}

      {/* 📦 Delivery Points */}
      {data.delivery_points.map(d => (
        <Marker key={d.id} position={[d.lat, d.lng]}>
          <Popup>{d.name}</Popup>
        </Marker>
      ))}
    </MapContainer>
  );
}

export default CampusMap;