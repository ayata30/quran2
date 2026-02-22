export default function Radio() {
  return (
    <div>
      <h2 className="text-2xl font-bold">Quran Radio</h2>
      <p>Live recitations coming soon…</p>
      <p>coming soon</p>
      <p>A loop of the Quran being recited by a Qari</p>

  <p className="text-gray-400 max-w mt-4 mx-auto">
    While the radio is being built, here’s a playlist
    of some of my favorite Quran recitations. </p>
    <p className="text-gray-400 mb-4 max mx-auto">
      Maybe you'll find one you like!
  </p>

<iframe
  title="Quran Playlist"
  width="85%"
  height="420"
  scrolling="no"
  frameBorder="0"
  autoplay="allow"
 
  src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/soundcloud%253Aplaylists%253A1825829712&color=%234feed5&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"

></iframe>

<p className="text-xs  text-center text-gray-400 mt-4 max-w-md max-auto mb-4 ">
  This embedded audio player is provided by SoundCloud and may use cookies
   & collect usage data for analytics purposes. By using this player, you
  acknowledge that third-party services may collect data in accordance
  with their policies.
</p>
    </div>
  );
}
