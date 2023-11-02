const data = async (req, res) => {
//   const { data } = req.body;
  console.log('SERVER', req.body);
//   const addContact = await service.addContact(req.body, _id);
  res.status(200).json({ message: "Node server got a data"});
};

module.exports = {
  data,
};
